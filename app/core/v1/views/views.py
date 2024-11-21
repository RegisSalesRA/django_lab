from rest_framework import generics
from core.models import Album, Task, Tag, Category
from core.v1.serializers.serializers import (
    AlbumCreateSerializer, AlbumListSerializer, TaskSerializer, TagSerializer, CategorySerializer,
    TaskCreateSerializer, TagCreateSerializer, CategoryCreateSerializer
)


class TasksView(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by('createdAt')
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


class AlbumsView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumListSerializer


class AlbumView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumCreateSerializer
