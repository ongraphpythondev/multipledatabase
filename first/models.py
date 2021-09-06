from django.db import models
# Create your models here.


class First(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=100)
    app_name = models.CharField(max_length=20, default='first_app')

    def __str__(self):
        return self.title
