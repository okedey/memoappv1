from unicodedata import category
from django.shortcuts import render
from django.shortcuts import redirect
from .models import study_web
from .forms import study_webForm
from django.core import serializers
import json
import ast

# Create your views here.


def web_home(request):
   if(request.method == 'POST'):
      keywords=request.POST['keywords']
      data=web_search(keywords)
   data = study_web.objects.all() 
   params = {
        'data': data,
   }
   return render(request, 'memo1/study_web.html',params)


def web_create(request):
   if (request.method == 'POST'):
         obj = study_web()
         web = study_webForm(request.POST,instance=obj)
         web.save()
         return redirect(to="web_home")
   return render(request,'memo1/study_web.html',params)


def web_delete(request):
   if(request.method=='POST'):
      num = int(request.POST['num'])
      web = study_web.objects.get(id=num)
      web.delete()
   return redirect(to='web_home')
      

def web_detail(request):
   num = int(request.POST['num'])
   data = study_web.objects.get(id=num)
   params = {
        'data': data,
   }
   return render(request, 'study/study_web_detail.html',params)




def web_edit(request,num):
   obj = study_web.objects.get(id=num)
   if (request.method == 'POST'):
         web = study_webForm(request.POST,instance=obj)
         web.save()
   
   return redirect(to='web_home') 

def web_edit(request,num):
   #num = int(request.POST['num'])
   obj = study_web.objects.get(id=num)
   if (request.method == 'POST'):
         web = study_webForm(request.POST,instance=obj)
         web.save()
   return redirect(to='web_home')


def web_search(keywords):
   return redirect(to='web_home')