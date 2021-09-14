from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class survey(models.Model):
    IMPRESSION = [
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Poor', 'Poor'),
        ('Worst', 'Worst'),
    ]
    
    code = models.CharField(max_length=10, verbose_name='Queue Code', help_text='Scan your Queue Code')
    rating = models.IntegerField(default=0, help_text='Input 1 to 5  only',
        validators = [
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    impression = models.CharField(max_length=20, choices=IMPRESSION)
    comments = models.TextField(max_length=255)
    posting_date = models.DateField(null=True, auto_now_add=True, verbose_name='Posting Date')

    def __str__(self):
        return f"{self.code} - {self.comments}"
        # return str(self.comments)
