from django.shortcuts import render
from django.views import generic
from base.models import Task


class TaskList(generic.ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'task_list.html'
    fields = ['title', 'description', 'complete']
