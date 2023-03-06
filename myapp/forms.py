from django import forms
from .models import Project

class CreateNewTask(forms.Form):
    title = forms.CharField(max_length=300, label="Title")
    description = forms.CharField(widget=forms.Textarea, label="Description")
    project = forms.ModelChoiceField(Project.objects)
class CreateNewProject(forms.Form):
    name = forms.CharField(max_length=200, label="Name")

