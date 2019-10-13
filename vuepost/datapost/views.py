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
    while compt <1000:
        compt += 1
    
    datas = {
        'success':issuccess,
        'name':name
    }
    
    
    return JsonResponse(datas, safe=False)


def postform(request):
    name = request.POST.get('name')
    username = request.POST.get('username')
    password = request.POST.get('password')
    passwordconf = request.POST.get('passwordconf')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    
    issucces = False
    
    if username is not None and name is not None and password is not None and email is not None and phone is not None and passwordconf is not None:
        image = request.FILES['file']
        issucces = True
        h = Utilisateur(nom=name,username=username,password=password,email=email,phone=phone,image=image)
        h.save()
        print(name,username,phone,email,password,passwordconf,image)
    else:
        issucces = False
    datas = {
        'succes': issucces,
        'name': name,
    }
    return JsonResponse(datas, safe=False)