from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    content = forms.CharField(max_length=100,label='', widget=forms.TextInput(attrs={'placeholder':'Add task here...'}),)
    class Meta:
        model = Task
        fields = ['content']


class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'