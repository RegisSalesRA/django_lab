from django.urls import path
from core_auth.v1.views import EventView, EventsView, OrganizerSignupView


urlpatterns = [
    path("organizer_signup", OrganizerSignupView.as_view()),
    path("events",
         EventsView.as_view()),
    path("event/<str:pk>",
         EventView.as_view()),]
