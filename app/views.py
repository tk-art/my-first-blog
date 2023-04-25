from django.shortcuts import render

# Create your views here.

def base(request):
  return render(request,'base.html')

def signup(request):
  return render(request,'signup.html')

def login(request):
  return render(request,'login.html')