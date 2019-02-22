from django.shortcuts import render
from django.conf import settings
from app.animal import *
from .models import *
import os

# Create your views here.
def loadanimal(request):
    return render(request, 'animal/loadanimal.html')

def getmg(request):
    pic = request.FILES.get('pic')
    if pic:
        path = os.path.join(settings.MEDIA_ROOT, 'animal/'+pic.name)
        with open(path, 'wb') as f:
            for p in pic.chunks():
                f.write(p)
        ani = Animal()
        res = ani.msg(path)
        man_msg = AnimalMsg()
        man_msg.name = pic.name
        man_msg.msg = res
        man_msg.save()
        src = '/static/media/animal/'+pic.name
        return render(request, 'animal/showmsg.html', context={'src':src, 'res':res})
    else:
        return render(request, 'animal/loadanimal.html', context={'msg':'请上传照片'})
