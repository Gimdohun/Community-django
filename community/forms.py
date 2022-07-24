from django.forms import ModelForm
from .models import Room, UserInfo

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class RegisterForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = '__all__'