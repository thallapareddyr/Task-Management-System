from .models import *

def get_user_tasks(user_instance):
    user_tasks = Tasks.objects.filter(created_by=user_instance.user).select_related('task_category')

    formatted_tasks = []
    for task in user_tasks:
        formatted_task = {
            "id": task.id,
            'title': task.title,
            'description': task.description,
            'created_on': task.created_on.strftime('%Y-%m-%d %H:%M:%S'),  # Format as needed
            'due_on': task.due_on.strftime('%Y-%m-%d %H:%M:%S'),  # Format as needed
            'category': task.task_category.name,
            'created_by': task.created_by
        }
        formatted_tasks.append(formatted_task)
    return formatted_tasks