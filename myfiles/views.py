from os import name

from django.shortcuts import render
from .models import *
# Create your views here.

def index(malumot):
    malumotlar = Portfolio.objects.all()
    services = Services.objects.all()
    teamdd = Team.objects.all()
    return render(malumot,'index.html',{'portfolio':malumotlar,'services':services,'teamdd':teamdd})

def portfolio(malumot,id):
    data = Portfolio.objects.get(id=id)
    return render(malumot,'portfolio-details.html',{'work':data})

def services(malumot):
    return render(malumot,'index.html')

def team(malumot):
    return render(malumot,'index.html')

def contact1(malumot):
    if malumot.method == 'POST':
        name = malumot.POST.get('name')
        email = malumot.POST.get('email')
        subject = malumot.POST.get('subject')
        message = malumot.POST.get('message')


        Contact(name=name,email=email,desc=message,fan=subject,).save()
    return render(malumot,'index.html')

def adminga_murojaat(malumot):

    return render(malumot,'index.html')


