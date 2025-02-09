from rest_framework import generics
from core.models import Task, Tag, Category
from core.v1.serializers.serializers import (
    TaskSerializer,
    TagSerializer,
    CategorySerializer, TaskCreateSerializer, TagCreateSerializer, CategoryCreateSerializer
)


class TasksView(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by(
        'createdAt')
    serializer_class = TaskCreateSerializer


class TaskView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TagsView(generics.ListCreateAPIView):
    queryset = Tag.objects.all().order_by('createdAt')
    serializer_class = TagCreateSerializer


class TagView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CategorysView(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by('createdAt')
    serializer_class = CategoryCreateSerializer


class CategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
