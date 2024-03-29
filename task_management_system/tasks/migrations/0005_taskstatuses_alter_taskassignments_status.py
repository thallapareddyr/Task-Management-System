# Generated by Django 5.0 on 2024-01-09 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0004_remove_tasks_due_on_taskassignments"),
    ]

    operations = [
        migrations.CreateModel(
            name="TaskStatuses",
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
                    "status",
                    models.CharField(
                        choices=[
                            ("todo", "To Do"),
                            ("InProgress", "In Progress"),
                            ("Completed", "Completed"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="taskassignments",
            name="status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="task_statuses",
                to="tasks.taskstatuses",
            ),
        ),
    ]
