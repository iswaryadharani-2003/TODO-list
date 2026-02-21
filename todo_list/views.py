from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from . forms import *

# Create your views here.

def task(request):
    list_1 = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form= TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    view={'tasks':list_1, 'form': form}
    return render(request,'todo_list/list.html', view)

def update_list(request, i):
    task= Task.objects.get(id=i)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task')
    
    task= {'form':form}
    return render(request, 'todo_list/update.html',task)

def deleteTask(request, i):
    item = Task.objects.get(id=i)
    if request.method == 'POST':
        item . delete()
        return redirect('task')
    return render(request, 'todo_list/delete.html')