from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

@unauthenticated_user
def signinPage(request):
    
def signin(request):
    return render(request , 'waterbill/signin.html')

def latestl(request):
    return render(request , 'waterbill/latestl.html')

def latestqv(request):
    return render(request , 'waterbill/latestqv.html')

def oldl(request):
    return render(request , 'waterbill/oldl.html')

def oldqv(request):
    return render(request , 'waterbill/oldqv.html')

def profile(request):
    return render(request , 'waterbill/profile.html')
