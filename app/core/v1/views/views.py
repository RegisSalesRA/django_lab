from rest_framework import generics
from core.models import Task
from core.v1.serializers.serializers import TaskSerializer


class TaskView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
