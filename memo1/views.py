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
   json_data = serializers.serialize("json", study_web.objects.all())#データベースを文字列変換
   #json_data_list = ast.literal_eval(json_data)#辞書型として保存
   """ print(type(json_data_list))"""
   #print(json_data_list[0]["fields"])#python内ではjsonとして使用可能
   """ json_data_json=json.dumps(json_data_list,ensure_ascii=False) 
   print(json_data_json[0])
   print(type(json_data_json)) """
   data = study_web.objects.all() 
   params = {
        'title': 'Hello',
        'data': data,
   }
   return render(request, 'memo1/study_web.html',params)


def web_create(request):
   params = {
        'title': 'Hello',
    }
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
        'title': 'Hello',
        'data': data,
   }
   return render(request, 'study/study_web_detail.html',params)




def web_edit(request,num):
   #num = int(request.POST['num'])
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