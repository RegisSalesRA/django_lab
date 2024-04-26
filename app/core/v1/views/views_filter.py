from rest_framework import generics
from core.models import Task
from core.v1.serializers.serializers import TaskSerializer
from django.db.models import Count


class TaskByCategoryView(generics.ListAPIView):

    serializer_class = TaskSerializer

    def get_queryset(self, *args, **kwargs):
        id = self.kwargs['pk']
        return Task.objects.filter(category_id=id).order_by('createdAt')


class TaskByTagView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        tag_ids = self.request.query_params.getlist('tags', [])

        queryset = Task.objects.all()

        if tag_ids:
            queryset = queryset.filter(tags__id__in=tag_ids)

        return queryset.annotate(tag_count=Count('tags')).filter(tag_count=len(tag_ids)).order_by('createdAt')
