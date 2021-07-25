from django.shortcuts import render, get_object_or_404
from todo.models import Todo
from todo.forms import TodoForm
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

#메인 화면 리스트 보여주기. 
def index(request):
    todo_list = Todo.objects.all().order_by('-todo_date')
    context = {'todo_list':todo_list}
    return render(request, 'todo/index.html', context)

#상세보기
def detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    context = {'todo':todo}
    return render(request, "todo/detail.html", context)

#등록하기
def enter(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            todo.todo_date = timezone.now()
            todo.save()
        return HttpResponseRedirect(reverse('todo:index'))
    elif request.method == 'GET':
        form = TodoForm()
        context = {'form':form}
        return render(request, 'todo/enter.html', context)

#수정하기
def update(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save()
            todo.todo_date = timezone.now()
            todo.save()
        return HttpResponseRedirect(reverse('todo:index'))
    else:
        form = TodoForm(instance=todo)
        context = {'form':form}
        return render(request, 'todo/update.html', context)

#삭제하기
def delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        todo.delete()
        return HttpResponseRedirect(reverse('todo:index'))
    return render(request, 'todo/delete.html', {'todo': todo})