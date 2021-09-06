from django.db import models

# Create your models here.
class surveys(models.Model):
    code = models.CharField(max_length=50)
    stars = models.IntegerField()
    comment_headers = models.CharField(max_length=255, null=True)
    comments = models.CharField(max_length=255)
    posting_date = models.DateField(null=True)