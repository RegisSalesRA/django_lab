from django.urls import path
from core_image.v1.views.views import AlbumsView


urlpatterns = [
    path("albums", AlbumsView.as_view()),
    ]
