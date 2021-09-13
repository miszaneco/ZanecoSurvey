from django.shortcuts import render, redirect
from .forms import SurveyForm
from .models import *

# Create your views here.
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

def surveys(request):
    return render(request, 'surveys.html', {})