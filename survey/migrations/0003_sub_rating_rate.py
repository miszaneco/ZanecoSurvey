# Generated by Django 2.2.10 on 2021-09-16 06:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20210916_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_rating',
            name='rate',
            field=models.IntegerField(default=0, help_text='Input 1 to 5  only', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
