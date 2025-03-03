from django.urls import path
from core_image.v1.views.views import AlbumView, AlbumsView


urlpatterns = [
    path("albums", AlbumsView.as_view()),
    path("album/<str:pk>", AlbumView.as_view()),
    ]
