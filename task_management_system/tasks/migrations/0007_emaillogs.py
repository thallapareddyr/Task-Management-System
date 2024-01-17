# Generated by Django 5.0 on 2024-01-17 06:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0006_alter_taskassignments_status_delete_taskstatuses"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailLogs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email_type",
                    models.CharField(
                        choices=[
                            ("task_assigned", "Task Assigned"),
                            ("task_status_updated", "Task Status Updated"),
                            ("task_due_date_updated", "Task Due Date Updated"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("success", "Success"), ("failed", "Failed")],
                        max_length=30,
                    ),
                ),
                (
                    "sent_to",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="email_sent_to",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "task_assignment_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tasks.taskassignments",
                    ),
                ),
            ],
        ),
    ]