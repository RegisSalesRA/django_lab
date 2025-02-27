from core_auth.models import EventModel, Organizer, User
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class OrganizerSerializerRegister(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True)
    email = serializers.EmailField(
        max_length=100, style={
            "input_type": "text"})
    name = serializers.CharField(max_length=255, style={"input_type": "text"})

    class Meta:
        model = User
        fields = ["username", "password", "password2", "email", "name"]
        extra_kwargs = {"password": {"write_only": True}}

    def save(self, **kwargs):

        user = User(username=self.validated_data["username"])
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if Organizer.objects.filter(
                email=self.validated_data["email"]).exists():
            raise serializers.ValidationError("Email already exist")

        if password != password2:
            raise serializers.ValidationError("Password do not match")

        try:
            user.set_password(password)
            user.is_organizer = True
            user.save()
            Organizer.objects.create(
                user=user,
                name=self.validated_data["name"],
                email=self.validated_data["email"])
            return user
        except Exception as e:
            print(e)
