from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from core_image.models import Album
from mocks.api_routes_image_mock import ApiRouteAuthMocks as routes
from PIL import Image
import io


class CoreImageAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.image = self.generate_valid_image()
        self.album_data = {"name": "Álbum de Teste", "image": self.image}

    def generate_valid_image(self):
        img = Image.new("RGB", (100, 100), color=(255, 0, 0))
        img_io = io.BytesIO()
        img.save(img_io, format="JPEG")
        img_io.seek(0)
        return SimpleUploadedFile("test_image.jpg", img_io.getvalue(), content_type="image/jpeg")

    def test_create_album_success(self):
        response = self.client.post(routes.url_api_get_auth_events(self), self.album_data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.content)
        album = Album.objects.first()
        self.assertIsNotNone(album)
        self.assertEqual(album.name, self.album_data["name"])

    def test_get_album_success(self):
        album = Album.objects.create(name="Teste de Álbum")
        response = self.client.get(routes.url_api_get_auth_event(self, album.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        self.assertEqual(response.json()["name"], album.name)

    def test_list_albums(self):
        Album.objects.create(name="Álbum 1")
        Album.objects.create(name="Álbum 2")
        response = self.client.get(routes.url_api_get_auth_events(self))
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        self.assertEqual(len(response.json()), 2)

    def test_update_album(self):
        album = Album.objects.create(name="Álbum Original")
        new_data = {"name": "Álbum Atualizado"}
        response = self.client.patch(routes.url_api_get_auth_event(self, album.id), new_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        album.refresh_from_db()
        self.assertEqual(album.name, new_data["name"])

    def test_delete_album(self):
        album = Album.objects.create(name="Álbum para Excluir")
        response = self.client.delete(routes.url_api_get_auth_event(self, album.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, response.content)
        self.assertFalse(Album.objects.filter(id=album.id).exists())

    def test_method_not_allowed(self):
        response = self.client.put(routes.url_api_get_auth_events(self), {"name": "Teste"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED, response.content)
