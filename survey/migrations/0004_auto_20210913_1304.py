# Generated by Django 2.2.10 on 2021-09-13 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20210913_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='posting_date',
            field=models.DateField(auto_created=True, null=True, verbose_name='Posting Date'),
        ),
    ]
