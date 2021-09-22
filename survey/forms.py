from django import forms
from django.forms import ModelForm
from .models import Survey, Sub_Rating


class FormSurvey(forms.ModelForm):
    class Meta:
        model = Survey
        # fields = '__all__'
        fields = ['code', 'rate', 'rate_type', 'comments']
        labels = {
            'code': 'Code',
            'rate': 'Rate',
            'rate_type': 'Rating',
            'comments': 'Comments',
        }
    
class FormSubRating(forms.ModelForm):
    class Meta:
        model = Sub_Rating
        # fields = '__all__'
        fields = ['rate', 'rate_type', 'sub_rating']
        labels = {
            'rate': '',
            'rate_type': '',
            'sub_rating': '',
        }