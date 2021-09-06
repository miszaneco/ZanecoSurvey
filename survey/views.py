from django.shortcuts import render

# Create your views here.
def page_surveys(response):
    return render(response, 'surveys.html', {})

def page_survey_new(response):
    return render(response, 'survey_new.html', {})
