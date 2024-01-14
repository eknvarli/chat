from django.shortcuts import render
from rooms.models import Room
from django.contrib.auth.decorators import login_required

@login_required
def view_room(request, room_slug):
    room = Room.objects.get(slug=room_slug)
    return render(request, 'rooms/room.jinja', context={
        'room':room,
    })