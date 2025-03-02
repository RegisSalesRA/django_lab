from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from core_auth.models import UserEvent
from rest_framework.views import APIView
from rest_framework.response import Response
from core_auth.v1.serializers import EventSerializer, UserProfileSerializer


class UserEventsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer

    def get_queryset(self):
        user = self.request.user.user_profile
        queryset = UserEvent.objects.filter(user=user)
        return queryset

    def post(self, request, *args, **kwargs):
        data = self.request.data
        user = self.request.user.user_profile

        try:
            UserEvent.objects.create(
                name=data["name"],
                reward=data["reward"],
                avilible=True,
                user=user
            )
            return Response(
                {"success": "Operação realizada com sucesso"},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response({"error": str(e), },
                            status=status.HTTP_400_BAD_REQUEST)


class UserEventView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer

    def get_object(self):
        user = self.request.user.user_profile
        event_id = self.kwargs.get("pk")
        print(event_id)
        return get_object_or_404(UserEvent, id=event_id, user=user.id)


class UserProfileView(generics.GenericAPIView):

    """
    This view is responsible to login with User user by application mobile and web
    """

    serializer_class = UserProfileSerializer

    def post(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {"result": "User account created successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                {"error": str(e), "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR})


class GetUser(APIView):
    """
    This view is responsible to create a Player user and can list then too insert this on database
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        content = {
            "id": user.id,
            "user": str(user),
        }

        return Response(content)
