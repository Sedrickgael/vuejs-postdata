from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import json

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