from django import forms
from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'task_category']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        # Exclude fields you don't want to display in the form
        exclude_fields = ['id', 'created_on', 'created_by']
        for field_name in exclude_fields:
            if field_name in self.fields:
                del self.fields[field_name]

class TaskAssignmentForm(forms.ModelForm):

    class Meta:
        model = TaskAssignments
        fields = ['task_id', 'assigned_to', 'due_on']
        exclude = ['status']
        widgets = {
            'due_on': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            # You might need to handle formatting or set specific date/time restrictions here
        }