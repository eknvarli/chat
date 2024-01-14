from django.shortcuts import render
from rooms.models import Room, Message
from django.contrib.auth.decorators import login_required

@login_required
def view_room(request, room_slug):
    room = Room.objects.get(slug=room_slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'rooms/room.jinja', context={
        'room':room,
        'messages':messages
    })