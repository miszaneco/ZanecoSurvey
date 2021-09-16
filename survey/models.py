from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid

# Create your models here.

class sub_rating(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    
    rate = models.IntegerField(default=0, help_text='Input 1 to 5  only',
        validators = [
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    rate_type = models.CharField(max_length=20)
    sub_rating = models.CharField(max_length=100)
    
    created_by = models.CharField(max_length=20, default='user')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=20, default='user')
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.rate} [{self.rate_type}] {self.sub_rating}"
    
class survey(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    
    RATING_TYPE = [
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Poor', 'Poor'),
        ('Worst', 'Worst'),
    ]
    
    code = models.CharField(max_length=10, verbose_name='Queue Code', help_text='Scan your Queue Code')
    
    rate = models.IntegerField(default=0, help_text='Input 1 to 5  only',
        validators = [
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    rate_type = models.CharField(max_length=20, choices=RATING_TYPE)
    sub_rating = models.TextField(max_length=255, null=True, blank=True)
    comments = models.TextField(max_length=255, null=True, blank=True)
    posting_date = models.DateField(null=True, auto_now_add=True, verbose_name='Posting Date')
    
    created_by = models.CharField(max_length=20, default='user')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=20, default='user')
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code} - {self.comments}"
