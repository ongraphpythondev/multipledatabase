# Generated by Django 3.1.7 on 2021-09-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='second',
            name='app_name',
            field=models.CharField(default='second_app', max_length=20),
        ),
    ]
