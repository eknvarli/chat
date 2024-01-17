from django import forms
from .models import Script


class WriteScriptForm(forms.ModelForm):
    class Meta:
        model = Script
        fields = ['name','content']