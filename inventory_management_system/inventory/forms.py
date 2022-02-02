from django import forms
from .models import *

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteers
        fields = ('name', 'phone', 'email', 'issues')


class ParticipateForm(forms.ModelForm):
    class Meta:
        model = Participates
        fields = ('name', 'phone', 'email', 'issues')
        

