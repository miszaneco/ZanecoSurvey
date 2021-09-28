from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FormSubRating, FormSurvey
from .models import Survey, Sub_Rating
import sweetify

from datetime import datetime, date

# Create your views here.
@login_required(login_url="/login/")
def index(request):
    today = datetime.today().date()
   
    context = {
        'surveyTodayExcellent': Survey.objects.filter(rate_type__contains='Excellent', posting_date=today).count(),
        'surveyTodayGood': Survey.objects.filter(rate_type__contains='Good', posting_date=today).count(),
        'surveyTodayFair': Survey.objects.filter(rate_type__contains='Fair', posting_date=today).count(),
        'surveyTodayPoor': Survey.objects.filter(rate_type__contains='Poor', posting_date=today).count(),
        
        'surveyExcellent': Survey.objects.filter(rate_type__contains='Excellent').count(),
        'surveyGood': Survey.objects.filter(rate_type__contains='Good').count(),
        'surveyFair': Survey.objects.filter(rate_type__contains='Fair').count(),
        'surveyPoor': Survey.objects.filter(rate_type__contains='Poor').count(),
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url="/login/")
def survey_create(request):
    if request.method == 'POST':
        form = FormSurvey(request.POST)

        if form.is_valid():
            object = form.save(commit=False)
            object.created_by = request.user.username
            object.save()
            args = dict(
                title='Submitted', 
                icon='success', 
                text="Good Job! The survey you just made has been successfully submitted. Thank You!", 
                timer=5000, 
                timerProgressBar='true', 
                persistent="Close"
            )
            sweetify.multiple(request, args)
            return redirect(survey_create)
    else:
        form = FormSurvey()
        sub_ratings = Sub_Rating.objects.all().values('sub_rating')
        
        context = {
            'form': form,
            'sub_ratings': sub_ratings,
        }
        
        return render(request, 'survey_create.html', context)
    
@login_required(login_url="/login/")
def survey_edit(request, uid):
    survey = Survey.objects.get(pk=uid)
    form = FormSurvey(request.POST or None, instance=survey)
    sub_ratings = Sub_Rating.objects.all().values('sub_rating')
    
    
    if request.method == 'POST':
        if form.is_valid():
            object = form.save(commit=False)
            object.updated_by = request.user.username
            object.save()
            return redirect(surveys)
    
    else:
        context = {
            'form': form,
            'survey': survey,
            'sub_ratings': sub_ratings,
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
def surveys_by_rate(request, rate_type):
    surveys = Survey.objects.raw(f"SELECT * FROM survey_survey WHERE rate_type LIKE '{rate_type}'")
    context = {
        'surveys': surveys
    }
    return render(request, 'surveys.html', context)

def surveys_by_rate_today(request, rate_type):
    today = datetime.today().date()
    surveys = Survey.objects.raw(f"SELECT * FROM survey_survey WHERE rate_type LIKE '{rate_type}' AND posting_date = '{today}'")
    context = {
        'surveys': surveys
    }
    return render(request, 'surveys.html', context)

@login_required(login_url="/login/")
def sub_rating_create(request):
    if request.method == 'POST':
        form = FormSubRating(request.POST)

        if form.is_valid():
            object = form.save(commit=False)
            object.created_by = request.user.username
            object.save()
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
        object.updated_by = request.user.username
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
    
