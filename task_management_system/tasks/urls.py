from django.urls import path
from . import views

urlpatterns = [
    path('create_task/', views.create_task, name='create_task'),
    path('<int:task_id>/details/', views.task_details, name='task_details'),
    path('<int:task_id>/update/', views.update_task, name='update_task'),
    path('<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('get_task_categories/', views.get_task_categories, name='get_task_categories'),

]