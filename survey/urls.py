from django.urls import path
from . import views

urlpatterns = [
    path('survey_new', views.createsurvey, name='survey_new'),
    path('surveys', views.surveys, name='surveys'),
]
