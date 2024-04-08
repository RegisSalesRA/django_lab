from django.urls import path
from core.v1.views.views import TaskView


urlpatterns = [

    path("tasks", TaskView.as_view()),]
