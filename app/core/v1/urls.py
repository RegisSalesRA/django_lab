from django.urls import path
from core.v1.views.views_filter import TaskByCategoryView, TaskByTagView
from core.v1.views.views import (
    TaskView, TasksView, CategorysView, CategoryView, TagsView, TagView
)


urlpatterns = [
    path("tasks", TasksView.as_view()),
    path("tasks/<str:pk>", TaskView.as_view()),
    path("tasks_by_category/<str:pk>", TaskByCategoryView.as_view()),
    path("tasks_by_tags", TaskByTagView.as_view()),
    path("tags", TagsView.as_view()),
    path("tags/<str:pk>", TagView.as_view()),
    path("categorys", CategorysView.as_view()),
    path("categorys/<str:pk>", CategoryView.as_view()),
    ]
