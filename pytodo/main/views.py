from django.shortcuts import render, redirect
from pytodo.main.forms import TaskForm
from pytodo.main.models import Task


def home(request):
    return render(request, 'home.html', {'task_list': Task.objects.all()})


def new_task(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'new_task.html', {'form': form})
