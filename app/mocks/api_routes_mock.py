from abc import ABC, abstractmethod


class ApiRouteInterface(ABC):
    @property
    @abstractmethod
    def url_api_get_tasks(self):
        pass


class ApiRouteMocks(ApiRouteInterface):
    @property
    def url_api_get_tasks(self):
        return '/api/v1/core/tasks'
