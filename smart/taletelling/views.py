from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
import os
import app.tell

# Create your views here.

def index(request):
    if os.listdir('static/media/'):
        for img in os.listdir('static/media/'):
            if os.path.isfile('static/media/'+img):
                os.remove('static/media/'+img)
    for img in os.listdir('static/media/img/'):
        os.remove('static/media/img/' + img)
    for img in os.listdir('static/media/star/'):
        os.remove('static/media/star/' + img)
    for img in os.listdir('static/media/animal/'):
        os.remove('static/media/animal/' + img)
    return render(request, 'index.html')

def story(request):
    s = Stories.objects.all()
    context = {'s': s}
    return render(request, 'story/story.html', context=context)

def talk(request):
    name = request.POST.get('s')
    try:
        app.tell.robot(name)
        return redirect('/smart/index/')
    except Exception:
        return redirect('/smart/index/')
