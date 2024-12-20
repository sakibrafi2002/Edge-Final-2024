from django.views.generic import ListView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from .models import Task
from .serializers import TaskSerializer

class ProjectTasksView(ListView):
    model = Task
    template_name = 'project_task.html'
    context_object_name = 'tasks'

    def get_queryset(self):
       # project_id = self.kwargs['project_id']
        return Task.objects.all().order_by(
            # Order by priority using custom ordering
            'priority'  # This orders by the string value of 'priority'
        )
        
        
        
class TaskListAPIView(ListAPIView):
    queryset = Task.objects.all()  # Retrieve all Task objects
    serializer_class = TaskSerializer
    
class TaskCreateAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class TaskUpdateAPIView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'
    
    