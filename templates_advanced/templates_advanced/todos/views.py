from django.shortcuts import render, redirect

from templates_advanced.todos.forms import TodoForm
from templates_advanced.todos.models import Todo


def list_todos(request):
    context = {
        'todos': Todo.objects.all()
    }

    return render(request, 'todos/list_todos.html', context)


def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_todos')
    else:
        form = TodoForm()

    context = {
        'form': form,
    }

    return render(request, 'todos/create_todo.html', context)
