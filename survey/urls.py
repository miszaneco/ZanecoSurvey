from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('survey_create', views.survey_create, name='survey_create'),
    path('survey_edit/<uid>', views.survey_edit, name='survey_edit'),
    path('survey_delete/<uid>', views.survey_delete, name='survey_delete'),
    path('surveys', views.surveys, name='surveys'),
    path('surveys_by_rate/<str:rate_type>', views.surveys_by_rate, name='surveys_by_rate'),
    
    path('sub_rating_create', views.sub_rating_create, name='sub_rating_create'),
    path('sub_rating_edit/<uid>', views.sub_rating_edit, name='sub_rating_edit'),
    path('sub_rating_delete/<uid>', views.sub_rating_delete, name='sub_rating_delete'),
    path('sub_ratings', views.sub_ratings, name='sub_ratings'),
]
