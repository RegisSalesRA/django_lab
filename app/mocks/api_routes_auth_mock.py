from abc import ABC, abstractmethod


class ApiAuthRouteInterface(ABC):
    @abstractmethod
    def url_api_get_auth_events(self):
        pass

    @abstractmethod
    def url_api_get_auth_event(self, id):
        pass

    @abstractmethod
    def url_api_create_user(self):
        pass

    @abstractmethod
    def url_api_get_user(self, id):
        pass

    @abstractmethod
    def url_api_login(self):
        pass


class ApiRouteAuthMocks(ApiAuthRouteInterface):

    def url_api_get_auth_events(self):
        return '/api/v1/core_auth/user_events'

    def url_api_get_auth_event(self, id):
        return f'/api/v1/core_auth/user_event/{id}'

    def url_api_create_user(self):
        return '/api/v1/core_auth/user_profile'

    def url_api_get_user(self):
        return '/api/v1/core_auth/get_user'

    def url_api_login(self):
        return '/api/token/'
