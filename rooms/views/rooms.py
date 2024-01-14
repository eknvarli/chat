from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from rooms.models import Room
from django.core.paginator import Paginator
from django.db.models import Q

@login_required
def rooms(request):
    rooms = Room.objects.all()
    search = request.GET.get('search')
    page = request.GET.get('rooms')
    if search:
        rooms = rooms.filter(
            Q(name__contains=search) |
            Q(slug__contains=search)
        ).distinct()

    paginator = Paginator(rooms, 5)

    return render(request, 'rooms/rooms.jinja', context={
        'rooms':paginator.get_page(page)
    })