from core_image.v1.serializers.serializers import AlbumSerializer
from core_image.models import Album
from rest_framework import generics


class AlbumsView(generics.ListCreateAPIView):
    queryset = Album.objects.all().order_by(
        'createdAt')
    serializer_class = AlbumSerializer
