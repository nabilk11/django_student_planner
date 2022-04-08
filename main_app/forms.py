from dataclasses import fields
from wsgiref.headers import tspecials
from django import forms
from .models import Task



class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }
