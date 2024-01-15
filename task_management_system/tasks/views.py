from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import TaskAssignmentForm, TaskForm
from django.contrib import messages
from .models import *
from django.utils.dateparse import parse_datetime
from django.core.mail import send_mail
from django.template.loader import render_to_string


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            messages.success(request, "Task created successfully.")
            return redirect("home")
    else:
        form = TaskForm()

    return render(request, "tasks/create_task.html", {"form": form})


def get_task_categories(request):
    categories = TaskCategories.objects.values("id", "name")
    return JsonResponse({"categories": list(categories)})


def task_details(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)

    # Assuming you want specific fields to be sent to the frontend
    task_details = {
        "title": task.title,
        "description": task.description,
        # 'due_on': task.due_on.strftime("%Y-%m-%dT%H:%M"),  # Format date as ISO 8601
        # Add other fields as needed
    }

    return JsonResponse(task_details)


def update_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task Edited successfully.")
            return JsonResponse({"success": True})  # Respond with success
        else:
            messages.error(request, "Task Edit Failed.")
            return JsonResponse({"success": False})  # Respond with failure

    return JsonResponse(
        {"success": False}
    )  # If not a POST request, respond with failure


def delete_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)

    if request.method == "DELETE":
        task.delete()

        messages.success(request, "Task deleted successfully.")
        return JsonResponse({"success": True})  # Respond with success
    else:
        messages.error(request, "Task Delete Failed.")
        return JsonResponse({"success": False})  # Respond with failure


def assign_task(request):
    if request.method == "POST":
        form = TaskAssignmentForm(request.POST)

        if form.is_valid():
            task_assignment = form.save(commit=False)
            task_assignment.assigned_by = (
                request.user
            )  # Set the assigned_by user to the current logged-in user
            task_assignment.save()
            html_message = render_to_string(
                "emails/tasks/task_assigned.html",
                {
                    "name": task_assignment.assigned_to.username,  
                    "task_name": task_assignment.task_id.title,  
                    "assigned_name": task_assignment.assigned_by.username,  
                    "task_description": task_assignment.task_id.description,
                    "due_on": task_assignment.due_on,
                },
            )
            sent_count = send_mail(
                subject="A Task has been Assigned to You",
                message="",
                from_email="gowthambalu447@gmail.com",
                recipient_list=[task_assignment.assigned_to.email],
                html_message=html_message,
            )
            # Check if the email was sent successfully
            if sent_count > 0:
                print("\n\n Email sent successfully!", sent_count)
            else:
                print("Email was not sent.")

            return JsonResponse({"message": "Task assigned successfully"})
        else:
            print("Form is invalid!")
            print(form.errors)
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)


def update_user_task(
    request,
    task_assignment_id,
):
    task = get_object_or_404(TaskAssignments, id=task_assignment_id)
    print(f"{task=}")

    if request.method == "POST":
        task_status = request.POST.get("task_status")
        print(f"{task_status=}")
        task.status = task_status
        task.save()
        
        # Send Email
        html_message = render_to_string(
                "emails/tasks/task_status_change.html",
                {
                    "assigner": task.assigned_by.username,  
                    "task_name": task.task_id.title,  
                    "updated_status": task.status,
                },
            )
        sent_count = send_mail(
                subject="Task Status Update",
                message="",
                from_email="gowthambalu447@gmail.com",
                recipient_list=[task.assigned_by.email],
                html_message=html_message,
            )
        
        print("\nUser Task Email Count\n", sent_count)
        
        messages.success(request, "Task Updated successfully.")

    return JsonResponse(
        {"success": False}
    )  # If not a POST request, respond with failure


def update_other_user_task(
    request,
    task_id,
):
    task = get_object_or_404(TaskAssignments, id=task_id)
    print(f"{task=}")

    if request.method == "POST":
        due_on = request.POST.get("due_on")
        print(f"{due_on=}")
        task.due_on = due_on
        task.save()
        messages.success(request, "Task Updated successfully.")

    return JsonResponse(
        {"success": False}
    )  # If not a POST request, respond with failure


def delete_task_assigned_to_user(request, task_id):
    task = get_object_or_404(TaskAssignments, id=task_id)

    if request.method == "DELETE":
        task.delete()
    
        messages.success(request, "Task Assigned deleted successfully.")
        return JsonResponse({"success": True})  # Respond with success
    else:
        messages.error(request, "Task Assigned Delete Failed.")
        return JsonResponse({"success": False})  # Respond with failure
