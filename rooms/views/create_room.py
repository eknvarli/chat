from django.shortcuts import render, redirect
from rooms.models import Room
from rooms.forms import CreateRoomForm
from django.contrib.auth.decorators import login_required

@login_required
def create_room(request):
    if request.method == 'POST':
        form = CreateRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rooms')
    else:
        form = CreateRoomForm()

    return render(request, 'rooms/create-room.jinja', context={
        'form':form,
    })