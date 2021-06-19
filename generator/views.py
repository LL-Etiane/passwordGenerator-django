from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'generator/home.html',{'password':{'key':'4','word':'etiane'}})

def textGenerator(request):
    text  = ""
    characters = list('abcdefjhigklmnopqrstuvwxyzABCDEFJHIGKLMNOPQRSTUVWXYZ0123456789,;/!##$%^&*()__+')
    len = int(request.GET.get('lenght',6))

    for x in range(len):
        text += random.choice(characters)
    return render(request,'generator/generated.html',{'text':text})

def about(request):
    return render(request,'generator/about.html')
