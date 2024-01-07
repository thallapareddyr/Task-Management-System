from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import TaskForm
from django.contrib import messages
from .models import *

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


def get_task_categories(request):
    categories = TaskCategories.objects.values('id', 'name')
    return JsonResponse({'categories': list(categories)})

def task_details(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)

    # Assuming you want specific fields to be sent to the frontend
    task_details = {
        'title': task.title,
        'description': task.description,
        'due_on': task.due_on.strftime("%Y-%m-%dT%H:%M"),  # Format date as ISO 8601
        # Add other fields as needed
    }

    return JsonResponse(task_details)

def update_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task Edited successfully.')
            return JsonResponse({'success': True})  # Respond with success
        else:
            messages.error(request, 'Task Edit Failed.')
            return JsonResponse({'success': False})  # Respond with failure

    return JsonResponse({'success': False})  # If not a POST request, respond with failure

def delete_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    
    if request.method == 'DELETE':
        task.delete()
        
        messages.success(request, 'Task deleted successfully.')
        return JsonResponse({'success': True})  # Respond with success
    else:
        messages.error(request, 'Task Delete Failed.')
        return JsonResponse({'success': False})  # Respond with failure

    return JsonResponse({'success': False})  
