from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import create_sub_rating_form, create_survey_form
from .models import survey, sub_rating

# Create your views here.
@login_required(login_url="/login/")
def index(request):
    # return render(request, 'surveys.html', {})
    surveys_list = survey.objects.order_by('uid')
    context = {
        'objects': surveys_list
    }
    return render(request, 'surveys.html', context)

@login_required(login_url="/login/")
def create_survey(request):
    if request.method == 'POST':
        form = create_survey_form(request.POST)
        # print(form)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = create_survey_form()
        context = {'form': form}
        
        return render(request, 'create_survey.html', context)

@login_required(login_url="/login/")
def create_sub_rating(request):
    if request.method == 'POST':
        form = create_sub_rating_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect(sub_ratings)
    else:
        form = create_sub_rating_form()
        context = {'form': form}
        
        return render(request, 'create_sub_rating.html', context)

@login_required(login_url="/login/")
def sub_ratings(request):
    # return render(request, 'surveys.html', {})
    ratings_list = sub_rating.objects.order_by('-rate')
    context = {
        'objects': ratings_list
    }
    return render(request, 'sub_ratings.html', context)
    
