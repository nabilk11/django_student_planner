from django.contrib import admin
# import models
from .models import Collaborator, Event, NewsletterEmail, Task, Profile

# Register your models here.

admin.site.register(Event)
admin.site.register(Collaborator)
admin.site.register(Task)
admin.site.register(Profile)
admin.site.register(NewsletterEmail)