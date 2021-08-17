from django.forms import ModelForm
from manager.mod


class RegisterForm(ModelForm):

    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=PasswordInput)
    email = forms.CharField(widget=EmailInput)
    discord_id = forms.CharField(max_length=100, label='Discord ID')
    zoom_id = forms.CharField(max_length=100, label='Zoom ID')

class Meta:
    model = Person
    fields = ["username", "password", "birthdate", "email", "discord_id", "zoom_id"]