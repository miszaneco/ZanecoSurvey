from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import createSurveyForm
from .models import survey

# Create your views here.
@login_required(login_url="/login/")
def index(request):
    # return render(request, 'surveys.html', {})
    surveys_list = survey.objects.order_by('uid')
    context = {
        'objects': surveys_list
    }
    return render(request, 'surveys.html', context)

def rating(request):
    return render(request, 'rating.html')

@login_required(login_url="/login/")
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