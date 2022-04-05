from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from .models import Event
from datetime import datetime, timedelta, date
from calendar import HTMLCalendar, month
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.utils.safestring import mark_safe
import calendar
# Auth Imports
from django.contrib.auth.views import LoginView
# Login Mixin - passed into views to restrict
from django.contrib.auth.mixins import LoginRequiredMixin
# Register imports
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

# AUTH VIEWS - using class based views, may switch to function based in some instances
class Login(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('calendar')

# REGISTER VIEW
class Register(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('calendar')

    # form validation
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    # prevent logged in user from accessing register page
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('calendar')
        return super(Register, self).get(*args, **kwargs)


class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"  

# Calendar Utility - May move to separate file later?
# currently adds event to calendar based on created_at timing, possibly change to due_date?
class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()
# create day as table data || events filtered by days
    def formatday(self, day, events):
        daily_events = events.filter(due_date__day=day)
        d = ''
        for event in daily_events:
            d += f'<li><a class="cal-item" href="/events/{event.id}" > {event.title} </a></li>'
        if day != 0:
            return f'<td><span class="date">{day}</span><ul>{d}</ul></td>'
        return '<td></td>'

    # create week as a row of a table 
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'   

    # create month as a table || filtered by yr&m
    def formatmonth(self, request,  withyear=True):
        events = Event.objects.filter(user=request.user, due_date__year=self.year, due_date__month=self.month)

        cal = f'<table class="calendar" border="0" cellspacing="0" cellpadding="0">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal

# calendar / events view
class CalendarView(ListView):
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # today's date
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        # formatmonth to render calendar as a table
        html_cal = cal.formatmonth(self.request, withyear=True)
        context['calendar'] = mark_safe(html_cal) # in order to render html safe
        # context for month pagination
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

# next/previous month methods
def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

# Events List View - for user's event list
class EventList(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = context['events'].filter(user = self.request.user)
        context['count'] = context['events'].filter(completed = False).count()

        return context

# Event Detail View - Ind Event Details
class EventDetail(DetailView):
    model = Event
    template_name = 'event_detail.html'
    context_object_name = 'event'
    

# Event Create View - may have to alter with datetime of due date
class EventCreate(CreateView):
    model = Event
    template_name = 'event_form.html'
    fields = ['title', 'description', 'completed', 'due_date', 'event_type']
    success_url = reverse_lazy('calendar')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventCreate, self).form_valid(form)

# Update/Edit Event
class EventUpdate(UpdateView):
    model = Event
    template_name = 'event_update.html'
    fields = ['title', 'description', 'completed', 'due_date', 'event_type']
    success_url = reverse_lazy('calendar')

class EventDelete(DeleteView):
    model = Event
    template_name = 'event_confirm_delete.html'
    context_object_name = 'event'
    success_url = reverse_lazy('calendar')


# Collaborators



