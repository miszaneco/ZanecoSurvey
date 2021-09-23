from django import forms
from django.forms import ModelForm, widgets
from .models import Survey, Sub_Rating

SUB_RATING = Sub_Rating.objects.all().values('sub_rating', 'sub_rating')

SUB_RATINGS = []

for item in SUB_RATINGS:
    SUB_RATINGS.append(item)

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
        fields = ['code', 'rate', 'rate_type', 'comments']
        labels = {
            'code': 'Code',
            'rate': 'Rate',
            'rate_type': 'Rating',
            'sub_rating': 'Sub_Rating',
            'comments': 'Comments',
        }
        widgets = {
            'code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ABC123',
                }),
            'rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'rate_type': forms.Select(attrs={'class': 'form-control'}),
            'sub_rating': forms.Select(attrs={'class': 'form-control'}, choices=SUB_RATINGS),
            'comments': forms.TextInput(attrs={'class': 'form-control'}),
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
        widgets = {
            'rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'rate_type': forms.Select(attrs={'class': 'form-control'}),
            'sub_rating': forms.TextInput(attrs={'class': 'form-control'}),
        }