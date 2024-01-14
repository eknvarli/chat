from django.urls import path
from rooms.views import *

urlpatterns = [
    path('', rooms, name='rooms')
]