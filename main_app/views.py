from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Event
from datetime import datetime, timedelta
from calendar import HTMLCalendar
from django.views.generic import ListView
from django.utils.safestring import mark_safe

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"  

# Calendar Utility - May move to separate file later?
class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()
# create day as table data || events filtered by days
    def formatday(self, day, events):
        daily_events = events.filter(created_at__day=day)
        d = ''
        for event in daily_events:
            d += f'<li> {event.title} </li>'
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
    def formatmonth(self,  withyear=True):
        events = Event.objects.filter(created_at__year=self.year, created_at__month=self.month)

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
        d = get_date(self.request.GET.get('day', None))

        cal = Calendar(d.year, d.month)
        # formatmonth to render calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal) # in order to render html safe
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()










