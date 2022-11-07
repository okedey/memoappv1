from unicodedata import category
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

def login(request):
    return render(request,'login/signin_form.html')

def home(request):
    return render(request,'login/mypage_home.html')