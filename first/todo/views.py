from todo.models import Todo
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

class TodoList(ListView):
    template_name = 'todo/index.html'
    context_object_name = 'todo_list'
    def get_queryset(self): #QuerySet - custmizing
        return Todo.objects.all().order_by('-todo_date')

class TodoDetail(DetailView):
    Model = Todo
    template_name = 'todo/add.html'

class TodoEnter(CreateView):
    model = Todo
    template_name = 'todo/enter.html'
    success_url = reverse_lazy('todos:index')

class TodoUpdate(UpdateView):
    model = Todo
    template_name = 'todo/update.html'
    success_url = reverse_lazy('todo:index')

class TodoDelete(DeleteView):
    model = Todo
    template_name = 'todo/delete.html'
    success_url = reverse_lazy('todo:index')