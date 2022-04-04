from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    # AUTH URLS - Login + Register
    path('login/', views.Login.as_view(), name="login"),
    path('register/', views.Register.as_view(), name="register"),
    #LogoutView imported straight into urls.py
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    #Other Paths
    path('', views.Home.as_view(), name="home" ),
    path('about/', views.About.as_view(), name="about" ),
    path('calendar/', views.CalendarView.as_view(), name="calendar" ),
    path('events/', views.EventList.as_view(), name="events" ),
    path('events/<int:pk>/', views.EventDetail.as_view(), name="event_detail" ),
    path('events/new/', views.EventCreate.as_view(), name="event_create"),
    path('events/<int:pk>/edit/', views.EventUpdate.as_view(), name="event_update"),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name="event_delete"),




]