from django import forms
from .models import Game
from django.core.exceptions import ValidationError
import json

class MessageForm(forms.Form):
    # Every message should conform to this basic form. We use it as a base class for all the other forms about messaging
    messageType = forms.ChoiceField(required=True, choices=[('SCORE','score'), ('SAVE','save'), ('LOAD_REQUEST','load_request')], widget=forms.HiddenInput())
