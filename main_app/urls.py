from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    # AUTH URLS - Login + Register
    path('login/', views.Login.as_view(), name="login"),
    path('register/', views.Register.as_view(), name="register"),
    path('edit_profile/', views.UserEditView.as_view(), name="edit_profile"),

    #LogoutView imported straight into urls.py
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    #Other Paths
    path('', views.Home.as_view(), name="home" ),
    path('about/', views.About.as_view(), name="about" ),
    # Events | Calendar is for clanedar view for e
    path('calendar/', views.CalendarView.as_view(), name="calendar" ),
    path('events/', views.EventList.as_view(), name="events" ),
    path('events/<int:pk>/', views.EventDetail.as_view(), name="event_detail" ),
    path('events/new/', views.EventCreate.as_view(), name="event_create"),
    path('events/<int:pk>/edit/', views.EventUpdate.as_view(), name="event_update"),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name="event_delete"),
    # Collaborators
    path('collaborators/', views.CollaboratorsIndex.as_view(), name='collaborators'),
    path('collaborators/new/', views.AddCollaborator.as_view(), name='add_collaborator'),
    path('collaborators/<int:pk>/', views.CollaboratorDetail.as_view(), name='collaborator_detail'),
    path('collaborators/<int:pk>/edit/', views.CollaboratorUpdate.as_view(), name='collaborator_update'),
    path('collaborators/<int:pk>/delete/', views.CollaboratorDelete.as_view(), name='collaborator_delete'),
    # Event Tasks
    path('events/<int:pk>/addtask', views.AddTask.as_view(), name="add_task" ),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
    path('task/<int:pk>/edit/', views.TaskUpdate.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete'),
    path('task/<int:pk>/completed/', views.TaskCompleted.as_view(), name='task_completed'),
    


]