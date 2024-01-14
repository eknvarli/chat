from django.contrib.auth.forms import UserChangeForm
from core.models import CustomUser

class EditProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = CustomUser
        fields = ('email','username','avatar')