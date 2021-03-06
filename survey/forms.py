from django import forms
from django.forms import ModelForm, widgets
from .models import Survey, Sub_Rating

RATE_TYPE = [
    ('Excellent', 'Excellent'),
    ('Good', 'Good'),
    ('Fair', 'Fair'),
    ('Poor', 'Poor'),
    ('Worst', 'Worst'),
]

class FormSurvey(forms.ModelForm):
    class Meta:
        model = Survey
        # fields = '__all__'
        fields = ['code', 'rate', 'rate_type', 'sub_rating', 'comments']
        labels = {
            'code': 'Code',
            'rate': 'Rate',
            'rate_type': 'Rate Type',
            'sub_rating': 'Sub Rating',
            'comments': 'Comments',
        }
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control',}),
            'rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'rate_type': forms.Select(attrs={'class': 'form-control'}),
            'sub_rating': forms.Select(attrs={'class': 'form-control'}),
            'comments': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
class FormSubRating(forms.ModelForm):
    class Meta:
        model = Sub_Rating
        # fields = '__all__'
        fields = ['rate', 'rate_type', 'sub_rating']
        labels = {
            'rate': 'Rate',
            'rate_type': 'Rate Type',
            'sub_rating': 'Sub Rating',
        }
        widgets = {
            'rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'rate_type': forms.Select(attrs={'class': 'form-control'}),
            'sub_rating': forms.TextInput(attrs={'class': 'form-control'}),
        }