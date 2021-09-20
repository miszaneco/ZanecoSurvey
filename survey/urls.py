from django.urls import path
from survey import views

urlpatterns = [
    path('', views.index, name='index'),
    path('surveys', views.surveys, name='surveys'),
    path('surveys_by_rate/<int:rate>', views.surveys_by_rate, name='surveys_by_rate'),
    path('create_survey', views.create_survey, name='create_survey'),
    path('create_sub_rating', views.create_sub_rating, name='create_sub_rating'),
    path('sub_ratings', views.sub_ratings, name='sub_ratings'),
    # path('surveys', views.surveys, name='surveys'),
]
