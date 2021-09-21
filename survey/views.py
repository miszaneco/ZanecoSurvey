from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import create_sub_rating_form, create_survey_form
from .models import Survey, Sub_Rating

# Create your views here.
@login_required(login_url="/login/")
def index(request):
    return render(request, 'dashboard.html', {})

@login_required(login_url="/login/")
def survey_create(request):
    if request.method == 'POST':
        form = create_survey_form(request.POST)

        if form.is_valid():
            object = form.save(commit=False)
            object.save()
            return redirect('/')
    else:
        form = create_survey_form()
        context = {'form': form}
        
        return render(request, 'survey_create.html', context)
    
@login_required(login_url="/login/")
def survey_edit(request, uid):
    survey = Survey.objects.get(pk=uid)
    return render(request, 'survey_edit.html', {'surveys': survey})

def survey_delete(request, uid):
    survey = Survey.objects.get(pk=uid)
    survey.delete()
    return redirect('/')

@login_required(login_url="/login/")
def surveys(request):
    surveys_list = Survey.objects.order_by('posting_date')
    context = {
        'surveys': surveys_list
    }
    return render(request, 'surveys.html', context)

@login_required(login_url="/login/")
def surveys_by_rate(request, rate):
    if rate > 0:
        survey_list = Survey.objects.raw(f"SELECT * FROM survey_survey WHERE rate = '{rate}'")
        context = {
            'objects': survey_list
        }
        return render(request, 'surveys.html', context)



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
    ratings_list = Sub_Rating.objects.order_by('-rate')
    context = {
        'objects': ratings_list
    }
    return render(request, 'sub_ratings.html', context)
    
