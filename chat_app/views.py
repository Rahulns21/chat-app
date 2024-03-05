from django.shortcuts import render
from .models import *

def index(request):
    chatrooms = ChatRoom.objects.all()
    context = {'chatrooms': chatrooms}
    return render(request, 'chat_app/index.html', context=context)

def chatroom(request, slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room=chatroom)[0:30]
    context = {'chatroom': chatroom, 'messages': messages}
    return render(request, 'chat_app/room.html', context=context)