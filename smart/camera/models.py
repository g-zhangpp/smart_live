from django.db import models

# Create your models here.


class Image(models.Model):
    name = models.ImageField(upload_to='media')
    age = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    beauty = models.CharField(max_length=20)
    faceshape = models.CharField(max_length=20)

    def __str__(self):
        return self.name