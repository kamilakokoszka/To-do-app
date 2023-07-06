from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import generic, View
from django.views.generic import FormView

from base.models import Task
from base.forms import TaskForm
from django.contrib.auth.views import LoginView, LogoutView
from base.forms import UserCreationForm


class RegisterUserView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = '/login/'

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class UserLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    success_url = '/tasks/'

    def get_success_url(self):
        return reverse_lazy('task-list')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


class UserLogoutView(LogoutView):
    next_page = '/tasks/'


class TaskListView(generic.ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'task_list.html'
    fields = ['title', 'description', 'complete']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'].filter(user=self.request.user)
        return context


class TaskUpdateView(generic.UpdateView):
    template_name = 'task_update.html'
    model = Task
    fields = ['title', 'description', 'complete']
    context_object_name = 'task'
    success_url = '/tasks/'


class TaskCreateView(generic.CreateView):
    template_name = 'task_form.html'
    model = Task
    fields = ['title', 'description']
    success_url = '/tasks/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskDeleteView(generic.DeleteView):
    template_name = 'task_confirm_delete.html'
    model = Task
    context_object_name = 'task'
    success_url = '/tasks/'