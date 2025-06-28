import graphene
from graphene_django import DjangoObjectType
from .models import Fruit


class FruitType(DjangoObjectType):
    class Meta:
        model = Fruit
        fields = ("id", "name", "description", "price", "stock_quantity", "is_available", "created_at")


class Query(graphene.ObjectType):
    fruits = graphene.List(FruitType)

    def resolve_fruits(root, info, **kwargs):
        return Fruit.objects.all()


class CreateFruit(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()
        price = graphene.Decimal(required=True)
        stock_quantity = graphene.Int()
        is_available = graphene.Boolean()

    fruit = graphene.Field(FruitType)

    def mutate(self, info, name, description=None, price=0.0, stock_quantity=0, is_available=True):
        fruit = Fruit(
            name=name,
            description=description,
            price=price,
            stock_quantity=stock_quantity,
            is_available=is_available
        )
        fruit.save()
        return CreateFruit(fruit=fruit)


class UpdateFruit(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        description = graphene.String()
        price = graphene.Decimal()
        stock_quantity = graphene.Int()
        is_available = graphene.Boolean()

    fruit = graphene.Field(FruitType)

    def mutate(self, info, id, **kwargs):
        try:
            fruit = Fruit.objects.get(pk=id)
        except Fruit.DoesNotExist:
            raise Exception("Fruit not found")

        for key, value in kwargs.items():
            if value is not None:
                setattr(fruit, key, value)

        fruit.save()
        return UpdateFruit(fruit=fruit)


class DeleteFruit(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        try:
            fruit = Fruit.objects.get(pk=id)
            fruit.delete()
            return DeleteFruit(success=True)
        except Fruit.DoesNotExist:
            raise Exception("Fruit not found")


class Mutation(graphene.ObjectType):
    create_fruit = CreateFruit.Field()
    update_fruit = UpdateFruit.Field()
    delete_fruit = DeleteFruit.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
