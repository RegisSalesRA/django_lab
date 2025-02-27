from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from core_auth.models import EventModel
from rest_framework.response import Response
from core_auth.v1.serializers import EventSerializer, OrganizerSerializerRegister


class EventsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    queryset = EventModel.objects.all()


class EventView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    queryset = EventModel.objects.all()


class OrganizerSignupView(generics.GenericAPIView):

    """
    This view is responsible to login with Organizer user by application mobile and web
    """

    serializer_class = OrganizerSerializerRegister

    def post(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {"result": "Organizer account created successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                {"error": str(e), "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR})
