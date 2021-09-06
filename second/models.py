from django.db import models
# Create your models here.


class Second(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=100)
    app_name = models.CharField(max_length=20, default='second_app')

    def __str__(self):
        return self.title
