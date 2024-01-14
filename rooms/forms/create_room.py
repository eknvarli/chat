from django.forms import ModelForm
from rooms.models import Room

class CreateRoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ('name',)