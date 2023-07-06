from django.shortcuts import render
from django.views import generic
from base.models import Task
from base.forms import TaskForm


class TaskListView(generic.ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'task_list.html'
    fields = ['title', 'description', 'complete']


class TaskUpdateView(generic.UpdateView):
    template_name = 'task_update.html'
    model = Task
    context_object_name = 'task'
    success_url = '/tasks/'


class TaskCreateView(generic.CreateView):
    template_name = 'task_form.html'
    model = Task
    fields = ['title', 'description']
    success_url = '/tasks/'
