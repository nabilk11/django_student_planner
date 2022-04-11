from dataclasses import field
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Task


# NEW REGISTER FORM
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=55)
    last_name = forms.CharField(max_length=55)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2') 


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

