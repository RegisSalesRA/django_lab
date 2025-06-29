from django.db import models
from core_auth.models import UserProfile
from django.db.models import Prefetch


class ConversationManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().prefetch_related(
            Prefetch(
                'participants',
                queryset=UserProfile.objects.select_related('user').only('id', 'user__username')
            )
        )


class Conversation(models.Model):
    participants = models.ManyToManyField(UserProfile, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    objects = ConversationManager()

    def __str__(self):
        participant_names = " ,".join([user.user.username for user in self.participants.all()])
        return f'Conversation with {participant_names}'


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender.user.username} in {self.content[:20]}'
