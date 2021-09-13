from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SurveyForm
from .models import *

# Create your views here.
# def c(request):
#     return HttpResponse('This is a survey')

def index(request):
    return render(request, 'surveys.html', {})
    
def createsurvey(request):
    if request.method == 'POST':
        # print('sending survey information', request.POST)
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    form = SurveyForm()
    context = {'form': form}
    
    return render(request, 'createsurvey.html', context)

