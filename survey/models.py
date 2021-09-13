from django.db import models

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
    rating = models.IntegerField(help_text='Input 1 to 5  only')
    impression = models.CharField(max_length=20, choices=IMPRESSION)
    comments = models.TextField(max_length=255)
    posting_date = models.DateField(null=True, auto_created=True, verbose_name='Posting Date')

    def __str__(self):
        return f"{self.code} - {self.comments}"
        # return str(self.comments)
