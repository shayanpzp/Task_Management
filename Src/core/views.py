from django.shortcuts import render, get_object_or_404, redirect
from core.models import Category, Tag, Task
from .models import Task
from django.db.models import Q
from .forms import TaskForm




def all_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'all_tasks.html', {'tasks': tasks})


def search_tasks(request):
    query = request.GET.get('q')

    if query:
        tasks = Task.objects.filter(Q(title__icontains=query) | Q(tags__name__icontains=query))
    else:
        tasks = Task.objects.all()

    return render(request, 'search_tasks.html', {'tasks': tasks, 'query': query})


def view_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    return render(request, 'view_task.html', {'task': task})




def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_tasks')
    else:
        form = TaskForm()
    
    return render(request, 'add_task.html', {'form': form})



def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('all_tasks')

    return render(request, 'delete_task.html', {'task': task})



def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('all_tasks')
    else:
        form = TaskForm(instance=task)

    return render(request, 'edit_task.html', {'form': form, 'task': task})



