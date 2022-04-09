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

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'completed')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'decscription': forms.Textarea(attrs={'class': 'form-control'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }

class TaskCompleteForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('completed',)

        widgets = {
            'completed': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }

