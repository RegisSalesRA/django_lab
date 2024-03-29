from django.db import models

class Task(models.Model):

    name = models.CharField(max_length=255)

    createAt = models.DateTimeField(auto_now_add=True, auto_created=True)
    updateAt = models.DateTimeField(auto_now=True, auto_created=True)

    def __str__(self):
        return self.name
