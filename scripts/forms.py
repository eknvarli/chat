from django import forms
from .models import Script
from rooms.models import Room


class WriteScriptForm(forms.ModelForm):
    def __init__(self, owner, *args, **kwargs):
        super(WriteScriptForm, self).__init__(*args, **kwargs)
        self.owner = owner
        self.fields['room'].queryset = Room.objects.filter(owner=self.owner)

    class Meta:
        model = Script
        fields = ['name','content','room']