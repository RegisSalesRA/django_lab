from rest_framework import serializers
from core.models import Album, Task, Tag, Category


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TagCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AlbumCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"


class AlbumListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"

class AlbumCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"
