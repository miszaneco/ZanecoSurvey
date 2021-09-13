from django.urls import path
from . import views

urlpatterns = [
    path('createsurvey', views.createsurvey, name='createsurvey'),
    path('surveys', views.surveys, name='surveys'),
]
