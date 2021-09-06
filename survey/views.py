from django.shortcuts import render

# Create your views here.
def pagesurvey(response):
    return render(response, 'survey.html', {})

def pagesurveycreate(response):
    return render(response, 'surveycreate.html', {})
