from asyncio import Task
import email
from django.db import models
from django.contrib.auth.models import User
#phone_field from django-phone-field installation
from phone_field import PhoneField



# Create your models here.

# Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="profile_imgs")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return str(self.user)

#Collaborator Model
class Collaborator(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField(max_length=75)
    phone_number = PhoneField(blank=True)
    role = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name




# Event Model
TYPE_OPTIONS = (
    ("Work", "WORK"),
    ("School","SCHOOL"),
    ("Personal","PERSONAL"),
)

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    event_type = models.CharField(max_length=10, choices=TYPE_OPTIONS)
    #Add Collaborators to Event Model
    collaborators = models.ManyToManyField(Collaborator, blank=True)
    # #Add Tasks to Event Model
    # tasks = models.ManyToManyField('Task', blank=True)
    #view by title
    def __str__(self):
        return self.title

    #order based on completed status
    class Meta:
        ordering = ['completed']


# Event Task Model
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    event = models.ForeignKey(Event, related_name="tasks", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['completed']


# Newsletter Email Model
class NewsletterEmail(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

