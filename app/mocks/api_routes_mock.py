from abc import ABC, abstractmethod


class ApiRouteInterface(ABC):
    @abstractmethod
    def url_api_get_tasks(self):
        pass

    @abstractmethod
    def url_api_get_task(self, id):
        pass

    @abstractmethod
    def url_api_get_categories(self):
        pass

    @abstractmethod
    def url_api_get_category(self, id):
        pass

    @abstractmethod
    def url_api_get_tags(self):
        pass

    @abstractmethod
    def url_api_get_tag(self, id):
        pass

    @abstractmethod
    def url_api_get_tasks_by_category(self, id):
        pass

    @abstractmethod
    def url_api_get_tasks_by_tags(self, id):
        pass


class ApiRouteMocks(ApiRouteInterface):
    def url_api_get_tasks(self):
        return '/api/v1/core/tasks'

    def url_api_get_task(self, id):
        return f'/api/v1/core/tasks/{id}'

    def url_api_get_categories(self):
        return '/api/v1/core/categories'

    def url_api_get_category(self, id):
        return f'/api/v1/core/categories/{id}'

    def url_api_get_tags(self):
        return '/api/v1/core/tags'

    def url_api_get_tag(self, id):
        return f'/api/v1/core/tags/{id}'

    def url_api_get_tasks_by_category(self, id):
        return f'/api/v1/core/tasks_by_category/{id}'

    def url_api_get_tasks_by_tags(self, id):
        return f'/api/v1/core/tasks_by_tags/?tags={id}'
