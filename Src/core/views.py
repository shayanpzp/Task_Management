from django.shortcuts import render, get_object_or_404, redirect
from core.models import Category, Tag, Task
from .models import Task
from .forms import TaskForm

def all_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'all_tasks.html', {'tasks': tasks})

def search_tasks(request):
    
    return render(request, 'search_tasks.html')

def view_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    return render(request, 'view_task.html', {'task': task})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            
            
            if form.cleaned_data['category'] is None:
                
                task.category = Category.objects.get_or_create(name='Uncategorized')[0]

            task.save()
            return redirect('all_tasks')
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete_task()
    return redirect('all_tasks')
