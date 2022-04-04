from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home" ),
    path('about/', views.About.as_view(), name="about" ),
    path('calendar/', views.CalendarView.as_view(), name="calendar" ),
    path('events/', views.EventList.as_view(), name="events" ),
    path('events/<int:pk>/', views.EventDetail.as_view(), name="event_detail" ),
    path('events/new/', views.EventCreate.as_view(), name="event_create"),




]