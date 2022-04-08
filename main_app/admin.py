from django.contrib import admin
# import models
from .models import Collaborator, Event, Task

# Register your models here.

admin.site.register(Event)
admin.site.register(Collaborator)
admin.site.register(Task)