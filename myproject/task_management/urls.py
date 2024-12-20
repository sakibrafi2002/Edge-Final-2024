from django.urls import path,include
from django.views.generic import TemplateView

from .views import ProjectTasksView, TaskListAPIView, TaskCreateAPIView, TaskUpdateAPIView  

urlpatterns = [
    path('', ProjectTasksView.as_view(), name='tasks'),
    path('api/tasks/', TaskListAPIView.as_view(), name='task-list'),
    path('api/tasks/create/', TaskCreateAPIView.as_view(), name='task-create'),
    path('api/tasks/update/<int:id>/', TaskUpdateAPIView.as_view(), name='task-update'),
]