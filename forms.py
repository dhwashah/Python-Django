from django import forms
from django.forms import ModelForm
from models import Clients

class ClientsForm(ModelForm):
    class Meta:
       model = Clients
       fields = '__all__'

##############################

DISPLAY_CHOICES = (
   ("Update me !", "Update"),
)

class Myform(forms.Form):
    display_type = forms.ChoiceField(widget=forms.RadioSelect, choices=DISPLAY_CHOICES)
