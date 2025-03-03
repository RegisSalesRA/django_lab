from django.test import TestCase
from core_auth.models import UserEvent
from core_auth.tests.helpers.core_auth_helper import UserEventFactory, UserProfileFactory
from mocks.data_auth_mock import DataAuthMocks
from rest_framework import status
from rest_framework.test import APIClient
from mocks.api_routes_auth_mock import ApiRouteAuthMocks as routes


class CoreAuthLoginAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()
        user_profile = DataAuthMocks.data_user_create
        self.client.post(routes.url_api_create_user(self), user_profile, format="json")
        self.data = DataAuthMocks.data_user_login
        self.wrong_data = DataAuthMocks.data_user_create_wrong

    def test_login_user_success(self):
        response = self.client.post(routes.url_api_login(self), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)

    def test_login_user_method_delete_not_allowed(self):
        response = self.client.delete(routes.url_api_login(self), self.data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED, response.content)

    def test_login_user_method_put_not_allowed(self):
        response = self.client.put(routes.url_api_login(self), self.data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED, response.content)

    def test_login_user_fail(self):
        response = self.client.post(routes.url_api_login(self), self.wrong_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.content)

    def test_obtain_jwt_token_and_access_protected_route(self):
        response = self.client.post(routes.url_api_login(self), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        token = response.json()
        self.assertIsNotNone(token, "No token!")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token["access"]}')
        protected_response = self.client.get(routes.url_api_get_auth_events(self))
        self.assertEqual(protected_response.status_code, status.HTTP_200_OK, protected_response.content)

    def test_access_protected_route_without_token(self):
        response = self.client.get(routes.url_api_get_auth_events(self))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, response.content)

    def test_refresh_token(self):
        response = self.client.post(routes.url_api_login(self), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)

        refresh_token = response.json().get("refresh")
        self.assertIsNotNone(refresh_token, "Refresh token não foi gerado!")

        refresh_response = self.client.post("/api/token/refresh/", {"refresh": refresh_token}, format="json")
        self.assertEqual(refresh_response.status_code, status.HTTP_200_OK, refresh_response.content)
        self.assertIn("access", refresh_response.json(), "Novo token de acesso não foi retornado!")


class CoreUserEventTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user_event_data = {
            "name": "Evento Teste",
            "reward": "Recompensa Teste",
            "avilible": True,
            "user": None}
        self.user_profile = UserProfileFactory.create()
        self.user_event_data["user"] = self.user_profile.id

    def test_create_user_event(self):

        response = self.client.post(routes.url_api_login(self), {
            'username': self.user_profile.user.username,
            'password': 'password'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        token = response.json()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token["access"]}')
        response = self.client.post(routes.url_api_get_auth_events(self), self.user_event_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.content)
        event = UserEvent.objects.first()
        self.assertEqual(event.name, self.user_event_data["name"])
        self.assertEqual(event.reward, self.user_event_data["reward"])
        self.assertTrue(event.avilible)

    def test_update_user_event(self):
        response = self.client.post(routes.url_api_login(self), {
            'username': self.user_profile.user.username,
            'password': 'password'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        token = response.json()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token["access"]}')
        event = UserEventFactory.create(user=self.user_profile)
        self.assertIsNotNone(event.id)
        updated_data = {
            "name": "Evento Atualizado",
            "reward": "Recompensa Atualizada",
            "avilible": False,
            "user": self.user_profile.id
        }
        response = self.client.put(routes.url_api_get_auth_event(self, event.id), updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        event.refresh_from_db()
        self.assertEqual(event.name, updated_data["name"])
        self.assertEqual(event.reward, updated_data["reward"])
        self.assertFalse(event.avilible)

    def test_get_user_event(self):
        response = self.client.post(routes.url_api_login(self), {
            'username': self.user_profile.user.username,
            'password': 'password'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        token = response.json()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token["access"]}')
        event = UserEventFactory.create(user=self.user_profile)
        self.assertIsNotNone(event.id)
        response = self.client.get(routes.url_api_get_auth_event(self, event.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        data = response.json()
        self.assertEqual(data["name"], event.name)
        self.assertEqual(data["reward"], event.reward)
        self.assertEqual(data["avilible"], event.avilible)
        self.assertEqual(data["user"], self.user_profile.id)

    def test_delete_user_event(self):
        response = self.client.post(routes.url_api_login(self), {
            'username': self.user_profile.user.username,
            'password': 'password'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        token = response.json()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token["access"]}')
        event = UserEventFactory.create(user=self.user_profile)
        self.assertIsNotNone(event.id)
        response = self.client.delete(routes.url_api_get_auth_event(self, event.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, response.content)
        self.assertFalse(UserEvent.objects.filter(id=event.id).exists())
