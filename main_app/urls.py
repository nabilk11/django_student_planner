from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    # AUTH URLS
    path('login/', views.Login.as_view(), name="login"),

    path('', views.Home.as_view(), name="home" ),
    path('about/', views.About.as_view(), name="about" ),
    path('calendar/', views.CalendarView.as_view(), name="calendar" ),
    path('events/', views.EventList.as_view(), name="events" ),
    path('events/<int:pk>/', views.EventDetail.as_view(), name="event_detail" ),
    path('events/new/', views.EventCreate.as_view(), name="event_create"),
    path('events/<int:pk>/edit/', views.EventUpdate.as_view(), name="event_update"),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name="event_delete"),




]