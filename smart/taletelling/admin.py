from django.contrib import admin
from .models import *

# Register your models here.
class StoriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'file']
admin.site.register(Stories, StoriesAdmin)
