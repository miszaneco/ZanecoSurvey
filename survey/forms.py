from django import forms
from django.forms import ModelForm
from .models import survey

class SurveyForm(forms.ModelForm):
    class Meta:
        model = survey
        fields = ['code', 'rating', 'impression', 'comments']
