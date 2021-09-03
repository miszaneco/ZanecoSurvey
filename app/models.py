# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class surveys(models.Model):
    code = models.CharField(max_length=50)
    stars = models.IntegerField()
    comment_headers = models.CharField(max_length=255, null=True)
    comments = models.CharField(max_length=255)
    posting_date = models.DateField(null=True)
    
    #def __str__(self):
    #    return self.text
    
    #class Meta: 'Surveys'
    