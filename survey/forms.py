from django import forms
from django.forms import ModelForm
from .models import survey, sub_rating


class create_survey_form(forms.ModelForm):
    class Meta:
        model = survey
        # fields = '__all__'
        fields = ['code', 'rate', 'rate_type', 'comments']


class create_sub_rating_form(forms.ModelForm):
    class Meta:
        model = sub_rating
        # fields = '__all__'
        fields = ['rate', 'rate_type', 'sub_rating']