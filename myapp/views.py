from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request):
    return HttpResponse("Hello World")

def about(request):
    return HttpResponse("About")
def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })
