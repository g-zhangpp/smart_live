from django.contrib import admin
from .models import *

# Register your models here.
class ImgAdmin(admin.ModelAdmin):
    list_display = ['name', 'text']
admin.site.register(Img, ImgAdmin)
