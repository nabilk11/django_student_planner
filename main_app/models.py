from django.db import models
from django.contrib.auth.models import User
#phone_field from django-phone-field installation
from phone_field import PhoneField



# Create your models here.

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
    collaborators = models.ManyToManyField(Collaborator)

    #view by title
    def __str__(self):
        return self.title

    #order based on completed status
    class Meta:
        ordering = ['completed']