# todo_app/urls.py
from django.urls import path
from myapp import views

urlpatterns = [
    path('task-list/', views.task_list, name='task_list'),
    path('add-task/', views.add_task, name='add_task'),
    path('edit-task/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete-task/<int:pk>/', views.delete_task, name='delete_task'),
]
