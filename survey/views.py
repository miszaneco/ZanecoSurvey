from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import createSurveyForm
from .models import *

# Create your views here.
def index(request):
    return render(request, 'surveys.html',{})

def createsurvey(request):
    if request.method == 'POST':
        form = createSurveyForm(request.POST)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = createSurveyForm()
        context = {'form': form}
        
        return render(request, 'createsurvey.html', context)

