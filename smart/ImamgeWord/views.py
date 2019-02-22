from django.shortcuts import render
from django.conf import settings
from app.WORD import *
from .models import *
import os

# Create your views here.
def loadPage(request):
    return render(request, 'imgWord/loadPage.html')

def word(request):
    pic = request.FILES.get('pic')
    if pic:
        path = os.path.join(settings.MEDIA_ROOT, 'img/'+pic.name)
        with open(path, 'wb') as f:
            for p in pic.chunks():
                f.write(p)
        result = img_word(path)
        context = {'result':result}
        img = Img()
        img.name = pic.name
        img.text = request
        img.save()
        return render(request, 'imgWord/showWord.html', context=context)
    else:
        return render(request, 'imgWord/loadPage.html', context={'word':'请上传图片'})
