from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
class TaskViewSet(viewsets.ModelViewSet):
    queryset           = Task.objects.all()
    serializer_class   = TaskSerializer
    http_method_names  = ['get', 'post', 'patch', 'delete', 'head', 'options']
    @action(detail=False, methods=['get'], url_path='stats')
    def stats(self, request):
        total     = Task.objects.count()
        completed = Task.objects.filter(completed=True).count()
        return Response({
            'total':     total,
            'completed': completed,
            'pending':   total - completed,
        })
