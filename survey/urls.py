from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('survey_create', views.survey_create, name='survey_create'),
    path('survey_edit/<uid>', views.survey_edit, name='survey_edit'),
    path('survey_delete/<uid>', views.survey_delete, name='survey_delete'),
    path('surveys', views.surveys, name='surveys'),
    path('surveys_by_rate/<int:rate>', views.surveys_by_rate, name='surveys_by_rate'),
    
    path('create_sub_rating', views.create_sub_rating, name='create_sub_rating'),
    path('sub_ratings', views.sub_ratings, name='sub_ratings'),
]
