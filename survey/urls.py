from django.urls import path
from . import views

urlpatterns = [
    path('surveys', views.page_surveys, name='surveys'),
    path('survey_new', views.page_survey_new, name='survey_new'),
]
