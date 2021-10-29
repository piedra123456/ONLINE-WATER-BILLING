from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Consumerlist
from .models import *
from django.contrib import messages

# Create your views here.

def signin(request):
    results = None
    query = request.POST.get('meter_number')
    if request.method == "POST":
        if query:
            if Consumerlist.objects.filter(meter_number = query).exists():
                results = Consumerlist.objects.get(meter_number = query)
                return redirect('latestl')
                return render(request, 'waterbill/latestl.html', {'query': query, 'results': results})
            else:
                messages.info(
                request, 'The meter number you’ve entered is incorrect. Please try again.')


    return render(request, 'waterbill/signin.html', {'query': query, 'results': results})




def latestl(request):
    user_infos = Consumerlist.objects.all()

    context = {"user_infos":user_infos}

    return render(request, 'waterbill/latestl.html', context)



def oldl(request):
    return render(request , 'waterbill/oldl.html')



def profile(request):
    return render(request , 'waterbill/profile.html')
