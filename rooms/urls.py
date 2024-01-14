from django.urls import path
from rooms.views import *

urlpatterns = [
    path('', rooms, name='rooms'),
    path('create/', create_room, name='create_room'),
    path('<slug:room_slug>/', view_room, name='view_room')
]