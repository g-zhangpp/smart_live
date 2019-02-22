from django.shortcuts import render
from django.conf import settings
from app.man import *
from .models import *
import os

# Create your views here.
def loadman(request):
    return render(request, 'man/loadman.html')

def getmsg(request):
    pic = request.FILES.get('pic')
    if pic:
        path = os.path.join(settings.MEDIA_ROOT, 'star/'+pic.name)
        with open(path, 'wb') as f:
            for p in pic.chunks():
                f.write(p)
        person = Human()
        res = person.msg(path)
        man_msg = ManMsg()
        man_msg.name = pic.name
        man_msg.msg = res
        man_msg.save()
        src = '/static/media/star/'+pic.name
        return render(request, 'man/showmsg.html', context={'src':src, 'res':res})
    else:
        return render(request, 'man/loadman.html', context={'msg':'请上传照片'})

