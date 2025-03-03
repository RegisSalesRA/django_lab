from core_auth.models import User, UserEvent, UserProfile
import factory
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Faker('user_name')
    password = factory.PostGeneration(lambda obj, create, extracted, **kwargs: obj.set_password('password'))
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class UserProfileFactory(DjangoModelFactory):
    class Meta:
        model = UserProfile

    user = factory.SubFactory(UserFactory)
    name = factory.Faker('first_name')
    second_name = factory.Faker('last_name')
    email = factory.Faker('email')


class UserEventFactory(DjangoModelFactory):
    class Meta:
        model = UserEvent

    name = factory.Faker('word')
    reward = factory.Faker('sentence')
    avilible = factory.Faker('boolean')
    user = factory.SubFactory(UserProfileFactory)
