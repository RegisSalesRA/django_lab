import factory
from factory.django import DjangoModelFactory
from core.models import Task, Category, Tag


class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.Faker('word')


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')


class TaskFactory(DjangoModelFactory):
    class Meta:
        model = Task

    name = factory.Faker('word')
    category = factory.SubFactory(CategoryFactory)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for tag in extracted:
                self.tags.add(tag)
