from django.db import models

# Create your models here.


# Event Model
TYPE_OPTIONS = (
    ("W", "WORK"),
    ("S", "SCHOOL"),
    ("P", "PERSONAL"),
)

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    event_type = models.CharField(max_length=10, choices=TYPE_OPTIONS)

    #view by title
    def __str__(self):
        return self.title

    #order based on completed status
    class Meta:
        ordering = ['completed']