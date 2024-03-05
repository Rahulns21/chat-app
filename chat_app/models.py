from django.db import models
from django.contrib.auth.models import User

class ChatRoom(models.Model):
    class Meta:
        verbose_name_plural = 'Chat Rooms'

    def __str__(self) -> str:
        return self.name

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

class ChatMessage(models.Model):
    class Meta:
        verbose_name_plural = 'Chat Message'
        ordering = ['date']

    def __str__(self) -> str:
        return f"{self.user.username} (Room - {self.room}): {self.message_content}"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    message_content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    