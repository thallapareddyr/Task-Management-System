from django.forms import model_to_dict
from django.shortcuts import render, redirect
from .forms import TaskForm
from django.contrib import messages

def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            messages.success(request, 'Task created successfully.')
            return redirect('home')
    else:
        form = TaskForm()

    return render(request, 'tasks/create_task.html', {'form': form})
