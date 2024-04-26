from rest_framework import generics
from core.models import Task, Tag, Category
from core.v1.serializers.serializers import (
    TaskSerializer, TagSerializer, CategorySerializer
)


class TasksView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskView(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TagsView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagView(generics.RetrieveDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CategorysView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryView(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
