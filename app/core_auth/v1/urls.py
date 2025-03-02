from django.urls import path
from core_auth.v1.views import UserEventView, UserEventsView, UserProfileView, GetUser


urlpatterns = [
    path("user_profile", UserProfileView.as_view()),
    path("get_user", GetUser.as_view()),
    path("user_events",
         UserEventsView.as_view()),
    path("user_event/<str:pk>",
         UserEventView.as_view()),]
