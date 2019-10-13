from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration,name='registration'),
    path('post', views.senddata,name='post'),
    path('postform', views.postform, name='postimage'),
]