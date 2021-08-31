# Generated by Django 2.2.10 on 2021-08-31 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Surveys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('stars', models.IntegerField()),
                ('comment_headers', models.CharField(max_length=255, null=True)),
                ('comments', models.CharField(max_length=255)),
                ('posting_date', models.DateField(null=True)),
            ],
        ),
    ]
