from django import forms
from django.contrib.auth.models import User
from booking.models import Ticket

class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('first_name', 'last_name', 'gender')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']