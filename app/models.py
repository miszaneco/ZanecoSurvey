# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Surveys(models.Model):
    code = models.CharField(max_length=50)
    stars = models.IntegerField()
    comments = models.CharField(max_length=255)
    posting_date = models.DateField(null=True)
    
    class Meta: 'Surveys'
    