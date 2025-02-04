from django.contrib import admin
from core.models import Category, Tag, Task

admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(Category)
