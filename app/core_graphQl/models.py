from django.db import models


class Client(models.Model):
    
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

