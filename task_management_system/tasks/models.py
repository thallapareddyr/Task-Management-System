from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class TaskCategories(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Tasks(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    created_on = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    task_category = models.ForeignKey(TaskCategories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class TaskAssignments(models.Model):
    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="assigned_to_tasks"
    )
    assigned_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="assigned_by_tasks"
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    due_on = models.DateTimeField()
    created_on = models.DateTimeField(default=timezone.now)


class EmailLogs(models.Model):
    EMAIL_TYPE = [
        ("task_assigned", "Task Assigned"),
        ("task_status_updated", "Task Status Updated"),
        ("task_due_date_updated", "Task Due Date Updated"),
    ]
    SENT_STATUS = [
        ("success", "Success"),
        ("failed", "Failed"),
    ]
    task_assignment_id = models.ForeignKey(TaskAssignments, on_delete=models.CASCADE)
    sent_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="email_sent_to"
    )
    email_type = models.CharField(max_length=30, choices=EMAIL_TYPE)
    status = models.CharField(max_length=30, choices=SENT_STATUS)
