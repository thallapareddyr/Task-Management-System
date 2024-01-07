from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class TaskCategories(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    created_on = models.DateTimeField(default=timezone.now)


class Tasks(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    created_on = models.DateTimeField(default=timezone.now)
    due_on = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    task_category = models.ForeignKey(TaskCategories, on_delete=models.CASCADE)
