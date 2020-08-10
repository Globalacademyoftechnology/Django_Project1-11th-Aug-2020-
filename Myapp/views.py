from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def header(request):
    return render(request,"header.html")

def base(request):
    return render(request,"base.html")

def gallery(request):
    return render(request,"myapp/gallery.html")

def about_us(request):
    return render(request,"Myapp/about_us.html")

def order(request):
    return render(request,"Myapp/order.html")

def sign_up(request):
    return render(request,"myapp/sign_up.html")

def login(request):
    return render(request,"Myapp/login.html")
