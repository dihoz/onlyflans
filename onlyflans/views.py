from django.shortcuts import render

def acerca(request):
    return render(request,'about.html',{})

def indice(request):
    return render(request,'index.html',{})

def welcome(request):
    return render(request,'welcome.html',{})

def base(request):
    return render(request,'base.html',{})

def flanes(request):
    return render(request,'flanes.html',{})