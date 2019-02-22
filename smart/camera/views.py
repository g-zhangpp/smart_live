from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from . import models
from app.faceKnown import *
import os

# Create your views here.

def loadImage(request):
    return render(request, 'camera/camera.html')

def getFace(request):
    im = request.FILES.get('img')
    if im:
        path = os.path.join(settings.MEDIA_ROOT, im.name)
        with open(path, 'wb') as f:
            for p in im.chunks():
                f.write(p)
        face = Image()
        img = models.Image()
        age, beauty, gender, faceshape = face.face_detection('static/media/'+im.name)
        img.name = im.name
        img.age = age
        img.beauty = beauty
        img.faceshape = faceshape
        img.gender = gender
        img.save()
        src = '/static/media/'+im.name
        context = {'src':src, 'age':age, 'beauty':beauty, 'gender':gender, 'faceshape':faceshape}
        return render(request, 'camera/showface.html', context=context)
    else:
        return render(request, 'camera/camera.html', context={'word':'请上传图片'})