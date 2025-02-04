from django.db import models
from app.core.models import recipe_image_file_path


class Album(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=recipe_image_file_path)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
