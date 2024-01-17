from .models import *

def get_user_tasks(user_instance):
    user_tasks = Tasks.objects.filter(created_by=user_instance.user).select_related('task_category')

    formatted_tasks = []
    for task in user_tasks:
        formatted_task = {
            "id": task.id,
            'title': task.title,
            'description': task.description,
            'created_on': task.created_on.strftime('%Y-%m-%d %H:%M:%S'),
            'category': task.task_category.name,
            'created_by': task.created_by
        }
        formatted_tasks.append(formatted_task)
    return formatted_tasks

def tasks_assigned_to_user(user_instance):
    assigned_tasks = TaskAssignments.objects.filter(assigned_to_id=user_instance.user).select_related(
        'task_id__task_category__name', 'task_id__created_by', 'assigned_to', 'assigned_by', 'status__status'
    ).values(
        'id','task_id', 'task_id__title', 'task_id__description', 'created_on', 'task_id__created_by__username',
        'task_id__task_category__name', 'assigned_to__username', 'status', 'due_on'
    )
    print(f'{assigned_tasks=}')
    return assigned_tasks

def tasks_assigned_by_current_user(request):
    current_user_id = request.user.id
    assigned_tasks = TaskAssignments.objects.filter(assigned_by_id=current_user_id).select_related(
        'task_id__task_category', 'task_id__created_by', 'assigned_to', 'assigned_by'
    ).values(
        'id','task_id', 'task_id__title', 'task_id__description', 'created_on', 'task_id__created_by__username',
        'task_id__task_category__name', 'assigned_to__username', 'status', 'due_on'
    )
    print(f'Other user {assigned_tasks=}')

    return assigned_tasks