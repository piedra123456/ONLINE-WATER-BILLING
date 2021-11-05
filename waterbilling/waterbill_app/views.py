from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Consumerlist
from .forms import ConsumerlistForm
from .models import *
from django.contrib import messages


# admin.
def loginpage(request):
    user = request.user
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('addAnnounce')
        else:
            messages.info(
                request, 'The username/password you’ve entered is incorrect.')

    context = {}
    return render(request , 'main/login.html', context)

def addpage(request):
    return render(request , 'billadmin/addAnnounce.html')

def announcepage(request):
    return render(request , 'billadmin/Announce.html')

def viewpage(request):
    return render(request , 'billadmin/viewAnnounce.html')

def updatepage(request):
    return render(request , 'billadmin/upAnnounce.html')

def deletepage(request):
    return render(request , 'billadmin/delAnnounce.html')








# Consumer.
def signinpage(request):
    results = None
    query = request.POST.get('meter_number')
    if request.method == "POST":
        if query:
            if Consumerlist.objects.filter(meter_number = query).exists():
                results = Consumerlist.objects.get(meter_number = query)
                return redirect('/consumer/' + query)
            else:
                messages.info(
                request, 'The meter number you’ve entered is incorrect. Please try again.')


    return render(request, 'main/signin.html', {'query': query, 'results': results})

def consumerpage(request, id):

    result = Consumerlist.objects.get(meter_number = id)

    return render(request, 'waterbill/consumer.html', {'result':result})

def latestpage(request):
    return render(request, 'waterbill/latestl.html')

def oldpage(request):
    return render(request , 'waterbill/oldl.html')

def announcementspage(request):
    return render(request , 'waterbill/Announcements.html')

def viewAnnouncementspage(request):
    return render(request , 'waterbill/viewAnnouncements.html')

def profilepage(request, id):

    result = Consumerlist.objects.get(meter_number = id)

    return render(request, 'waterbill/profile.html', {'result':result})




# logout.

def logoutpage(request):
    logout(request)
    return redirect('signin')

def logpage(request):
    logout(request)
    return redirect('login')
