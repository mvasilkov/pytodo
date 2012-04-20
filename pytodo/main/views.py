from django.shortcuts import render
from pytodo.main.models import Task


def home(request):
    return render(request, 'home.html', {'task_list': Task.objects.all()})
