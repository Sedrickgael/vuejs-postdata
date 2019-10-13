from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def registration(request):
    return render(request, 'registration.html')

def senddata(request):
    
    postdata = json.loads(request.body.decode('utf-8'))
    
    # name = postdata['name']
    
    name = postdata['name']
    username = postdata['username']
    email = postdata['email']
    phone = postdata['phone']
    password = postdata['password']
    passwordconf = postdata['password1']
    issuccess=False
    
    if username !='':
        issuccess=True
    else:
        issuccess=False
    
    compt=1
    while compt <10000000:
        compt += 1
    
    datas = {
        'success':issuccess,
        'name':name
    }
    
    
    return JsonResponse(datas, safe=False)


def postimage(request):
    nom = request.POST.get('nom')
    username = request.POST.get('user')
    password = request.POST.get('password')
    passwordconf = request.POST.get('passwordconf')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    
    issucces = False
    cont = 1
    
    if user is not None and nom is not None and password is not None and repass is not None and email is not None and contact is not None:
        image = request.FILES['file']
        issucces = True
        h = Register(nom=nom,user=user,password=password,repass=repass,email=email,contact=contact,image=image)
        h.save()
        print(nom,user,contact,email,password,repass,image)
    else:
        issucces = False

    while cont < 100000000:
        cont += 1

    datas = {
        'succes': True,
        'nom': nom,
        'cont': cont
    }
    return JsonResponse(datas, safe=False)