from django import forms
from .models import Participant
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'password','email')


class ParticipantForm(forms.ModelForm):
    class Meta():
        model = Participant
        fields = ('college','year', 'branch', 'contact')