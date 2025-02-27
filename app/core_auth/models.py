from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_organizer = models.BooleanField(default=False)
    createAt = models.DateTimeField(auto_now_add=True, auto_created=True)
    updateAt = models.DateTimeField(auto_now=True, auto_created=True)
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",
        blank=True,
    )

    def __str__(self):
        return str(self.username)


class Organizer(models.Model):
    user = models.OneToOneField(
        User,
        related_name="organizer",
        on_delete=models.CASCADE,
        unique=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    second_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, unique=True)
    createAt = models.DateTimeField(auto_now_add=True, auto_created=True)
    updateAt = models.DateTimeField(auto_now=True, auto_created=True)

    def __str__(self) -> str:
        return str(self.user)

    def __repr__(self):
        return str(self.user)


class EventModel(models.Model):
    name = models.CharField(max_length=150)
    reward = models.CharField(max_length=200)
    avilible = models.BooleanField(default=True)
    createAt = models.DateTimeField(auto_now_add=True, auto_created=True)
    updateAt = models.DateTimeField(auto_now=True, auto_created=True)

    def __str__(self):
        return f"Evento: {self.name}"

    def __repr__(self):
        return f"Evento: {self.name}"
