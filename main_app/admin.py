from django.contrib import admin
# import models
from .models import Collaborator, Event

# Register your models here.

admin.site.register(Event)
admin.site.register(Collaborator)