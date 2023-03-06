from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject
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
def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })

def show_project(request, id):
    project = Project.objects.get(id=id)
    tasks = project.task_set.all()
    return render(request, 'show_project.html', {
        'project': project,
        'tasks': tasks
    })
def mark_done(request, id):
    task = Task.objects.get(id=id)
    task.done = True
    task.save()
    return show_project(request, task.project.id)
def create_task(request):
    if request.method == "GET":
        return render(request, 'create_task.html', {
            'form': CreateNewTask
        })
    else:
        title = request.POST['title']
        description = request.POST['description']
        project_id = request.POST['project']

        Task.objects.create(title=title, description=description, project_id=project_id)
        return redirect('/tasks')
def create_project(request):
    if request.method == "GET":
        return render(request, 'create_project.html', {
            'form': CreateNewProject
        })
    else:
        name = request.POST['name']
        Project.objects.create(name=name)
        return redirect('projects')


