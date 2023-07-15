from django import forms
from .models import TodoTask

class TodoTaskForm(forms.ModelForm):
    class Meta:
        model = TodoTask
        fields = ['task', 'date']