from django.db import models

# Create your models here.
class Img(models.Model):
    name = models.ImageField(upload_to='img')
    text = models.TextField()

    def __str__(self):
        return self.name
