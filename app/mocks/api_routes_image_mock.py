from abc import ABC, abstractmethod


class ApiImageRouteInterface(ABC):
    @abstractmethod
    def url_api_get_images(self):
        pass

    @abstractmethod
    def url_api_get_image(self, id):
        pass


class ApiRouteAuthMocks(ApiImageRouteInterface):
    def url_api_get_auth_events(self):
        return f'/api/v1/core_image/albums'

    def url_api_get_auth_event(self, id):
        return f'/api/v1/core_image/album/{id}'
