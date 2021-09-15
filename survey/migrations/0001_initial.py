# Generated by Django 2.2.10 on 2021-09-15 08:57

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='impression',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('impression', models.CharField(max_length=20)),
                ('impressions', models.CharField(max_length=100)),
                ('created_by', models.CharField(default='user', max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_by', models.CharField(default='user', max_length=20)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='survey',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('code', models.CharField(help_text='Scan your Queue Code', max_length=10, verbose_name='Queue Code')),
                ('rating', models.IntegerField(default=0, help_text='Input 1 to 5  only', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('impression', models.CharField(choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor'), ('Worst', 'Worst')], max_length=20)),
                ('comments', models.TextField(blank=True, max_length=255, null=True)),
                ('posting_date', models.DateField(auto_now_add=True, null=True, verbose_name='Posting Date')),
                ('created_by', models.CharField(default='user', max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_by', models.CharField(default='user', max_length=20)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
