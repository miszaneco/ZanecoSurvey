from django import forms
from django.forms import ModelForm
from .models import Survey, Sub_Rating


class create_survey_form(forms.ModelForm):
    class Meta:
        model = Survey
        # fields = '__all__'
        fields = ['code', 'rate', 'rate_type', 'comments']
    
    # this function will be used for the validation
        def clean(self):
            # data from the form is fetched using super function
            super(Survey, self).clean()
            
            # extract the username and text field from the data
            code = self.cleaned_data.get('code')
            comments = self.cleaned_data.get('comments')
    
            # conditions to be met for the username length
            if len(code) < 3:
                self._errors['username'] = self.error_class([
                    'Minimum 5 characters required'])
            
            if len(comments) < 10:
                self._errors['text'] = self.error_class([
                    'Comments should contain a minimum of 10 characters'])
    
            # return any errors if found
            return self.cleaned_data


class create_sub_rating_form(forms.ModelForm):
    class Meta:
        model = Sub_Rating
        # fields = '__all__'
        fields = ['rate', 'rate_type', 'sub_rating']