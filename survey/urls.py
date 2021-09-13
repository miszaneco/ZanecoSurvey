from django.urls import path
from survey import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createsurvey/', views.createsurvey, name='createsurvey'),
    # path('surveys', views.surveys, name='surveys'),
]
