# accounts/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group

@receiver(post_save, sender=User)
def assign_employee_group(sender, instance, created, **kwargs):
    if created:
        employee_group = Group.objects.get(name='Employee')
        instance.save()  # Save the user first to ensure it has an id
        instance.groups.add(employee_group)
