from abc import ABC, abstractmethod


class ApiRouteInterface(ABC):
    @abstractmethod
    def url_api_get_tasks():
        pass


class ApiRouteMocks(ApiRouteInterface):
    def url_api_get_tasks():
        return '/api/v1/core/tasks'
