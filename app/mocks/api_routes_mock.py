from abc import ABC, abstractmethod


class ApiRouteInterface(ABC):
    @abstractmethod
    def url_api_get_tasks():
        pass

    @abstractmethod
    def url_api_get_task():
        pass


class ApiRouteMocks(ApiRouteInterface):
    def url_api_get_tasks():
        return '/api/v1/core/tasks'

    def url_api_get_task(id):
        return f'/api/v1/core/tasks/{id}'

    def url_api_get_categorys():
        return '/api/v1/core/categorys'

    def url_api_get_category(id):
        return f'/api/v1/core/categorys/{id}'

    def url_api_get_tags():
        return '/api/v1/core/tags'

    def url_api_get_tag(id):
        return f'/api/v1/core/tags/{id}'

    def url_api_get_tasks_by_category(id):
        return f'/api/v1/core/tasks_by_category/{id}'

    def url_api_get_tasks_by_tags(id):
        return f'/api/v1/core/tasks_by_tags/?tags={id}'
