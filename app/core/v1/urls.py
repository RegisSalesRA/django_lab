from django.urls import path
from core.v1.views.views import (
    TaskView, TasksView, CategorysView, CategoryView, TagsView, TagView
)


urlpatterns = [
    path("tasks", TasksView.as_view()),
    path("tasks/<str:pk>", TaskView.as_view()),
    path("tags", TagsView.as_view()),
    path("tags/<str:pk>", TagView.as_view()),
    path("categorys", CategorysView.as_view()),
    path("categorys/<str:pk>", CategoryView.as_view()),
    ]
