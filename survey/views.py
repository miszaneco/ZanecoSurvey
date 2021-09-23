from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FormSubRating, FormSurvey
from .models import Survey, Sub_Rating

# Create your views here.
@login_required(login_url="/login/")
def index(request):
    return render(request, 'dashboard.html', {})

@login_required(login_url="/login/")
def survey_create(request):
    if request.method == 'POST':
        form = FormSurvey(request.POST)

        if form.is_valid():
            object = form.save(commit=False)
            object.save()
            return redirect(surveys)
    else:
        form = FormSurvey()
        sub_ratings = Sub_Rating.objects.raw(f"SELECT * FROM survey_sub_ratings WHERE rate = 1")
        
        context = {
            'form': form
            
            }
        
        return render(request, 'survey_create.html', context)
    
@login_required(login_url="/login/")
def survey_edit(request, uid):
    survey = Survey.objects.get(pk=uid)
    form = FormSurvey(request.POST or None, instance=survey)
    
    if form.is_valid():
        object = form.save(commit=False)
        object.save()
        return redirect(surveys)
    
    context = {
        'form': form,
        'survey': survey,
    }
    return render(request, 'survey_edit.html', context)

def survey_delete(request, uid):
    survey = Survey.objects.get(pk=uid)
    survey.delete()
    return redirect(surveys)

@login_required(login_url="/login/")
def surveys(request):
    surveys = Survey.objects.order_by('posting_date')
    context = {
        'surveys': surveys
    }
    return render(request, 'surveys.html', context)

@login_required(login_url="/login/")
def surveys_by_rate(request, rate):
    if rate > 0:
        surveys = Survey.objects.raw(f"SELECT * FROM survey_survey WHERE rate = '{rate}'")
        context = {
            'surveys': surveys
        }
        return render(request, 'surveys.html', context)

@login_required(login_url="/login/")
def sub_rating_create(request):
    if request.method == 'POST':
        form = FormSubRating(request.POST)

        if form.is_valid():
            form.save()
            return redirect(sub_ratings)
    else:
        form = FormSubRating()
        context = {'form': form}
        
        return render(request, 'sub_rating_create.html', context)

@login_required(login_url="/login/")
def sub_rating_edit(request, uid):
    sub_rating = Sub_Rating.objects.get(pk=uid)
    form = FormSubRating(request.POST or None, instance=sub_rating)
    
    if form.is_valid():
        object = form.save(commit=False)
        object.save()
        return redirect(sub_ratings)
    
    context = {
        'sub_rating': sub_rating,
        'form': form,
    }
    return render(request, 'sub_rating_edit.html', context)

def sub_rating_delete(request, uid):
    sub_rating = Sub_Rating.objects.get(pk=uid)
    sub_rating.delete()
    return redirect(sub_ratings)

@login_required(login_url="/login/")
def sub_ratings(request):
    sub_ratings = Sub_Rating.objects.order_by('-rate')
    context = {
        'sub_ratings': sub_ratings
    }
    return render(request, 'sub_ratings.html', context)
    
