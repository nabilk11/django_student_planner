from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, PasswordChangeView


urlpatterns = [
    # AUTH URLS - Login + Register
    path('login/', views.Login.as_view(), name="login"),
    path('register/', views.Register.as_view(), name="register"),
    #LogoutView & PasswordChangeView imported straight into urls.py
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('<int:pk>/password/', PasswordChangeView.as_view(), name="change_password"),
    # User Profile Views
    path('profile/create/', views.ProfileCreate.as_view(), name="create_profile"),
    path('<int:pk>/edit_account/', views.EditAccountView.as_view(), name="edit_account"),
    path('<int:pk>/profile/', views.ProfileView.as_view(), name="profile"),
    path('<int:pk>/profile/edit/', views.EditProfileView.as_view(), name="edit_profile"),
    
    #Other Paths
    path('', views.newsletter_view, name="home" ),
    path('about/', views.About.as_view(), name="about" ),
    path('contact/', views.contact_view, name="contact" ),
    # Events | Calendar is for clanedar view 
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