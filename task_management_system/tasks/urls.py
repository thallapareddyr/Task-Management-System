from django.urls import path
from . import views

urlpatterns = [
    path('create_task/', views.create_task, name='create_task'),
    path('<int:task_id>/details/', views.task_details, name='task_details'),
    path('<int:task_id>/update/', views.update_task, name='update_task'),
    path('<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('get_task_categories/', views.get_task_categories, name='get_task_categories'),
    path('assign_task/', views.assign_task, name='assign_task'),
    path('<int:task_assignment_id>/update_user_task/', views.update_user_task, name='update_user_task'),
    path('<int:task_assignment_id>/update_other_user_task/', views.update_other_user_task, name='update_other_user_task'),
    path('<int:task_assignment_id>/delete_task_assigned_to_user/', views.delete_task_assigned_to_user, name='delete_task_assigned_to_user'),
]