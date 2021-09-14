from django import forms
from django.forms import ModelForm
from .models import survey

class createSurveyForm(forms.ModelForm):
    class Meta:
        model = survey
        fields = ['code', 'rating', 'impression', 'comments']
