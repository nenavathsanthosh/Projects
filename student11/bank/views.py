from bank.models import contact
from django.contrib import messages
from datetime import datetime
from django.shortcuts import render

# Create your views here.


def bank(request):
    return render(request, 'home.html')


def contactus(request):
    return render(request, 'contactus.html')


def contact1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        if all([name, email, phone, desc]) == True:
            contact3 = contact(name=name, email=email,
                               phone=phone, desc=desc, date=datetime.today())
            contact3.save()
            messages.success(
                request, 'your conern has been recieved. we will get back to you soon.')
            return render(request, 'contactus.html')
        else:
            messages.success(request, 'invalied details')
            return render(request, 'contactus.html')
