from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about),
    path('projects/', views.projects, name='projects'),
    path('tasks/', views.tasks, name='tasks'),
    path('project/<int:id>', views.show_project, name='show_project'),
    path('mark_done/<int:id>', views.mark_done, name='mark_done'),
    path('create_task/', views.create_task, name='create_task'),
    path('create_project/', views.create_project, name='create_project')
]
