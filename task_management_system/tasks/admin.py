from django.contrib import admin

from .models import *


admin.site.register(TaskCategories)
admin.site.register(Tasks)
admin.site.register(TaskAssignments)