from django.db import models

# Create your models here.
class ManMsg(models.Model):
    name = models.ImageField(upload_to='star')
    msg = models.TextField()

    def __str__(self):
        return self.name