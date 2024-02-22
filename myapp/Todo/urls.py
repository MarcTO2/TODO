from django.urls import path
from Todo import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Todos/', views.Todos, name='Todos'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('search/', views.search_tasks, name='search_tasks'),
]