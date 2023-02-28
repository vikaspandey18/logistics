from django.shortcuts import render
from django.contrib import messages
from contacts.models import *
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request,'logistics/index.html')


def about(request):
    return render(request,'logistics/about.html')


def services(request):
    return render(request,'logistics/services.html')


def pricing(request):
    return render(request,'logistics/pricing.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        if name != "" and email != "" and subject != "" and message !="":
            email = email.lower()
            contact = ContactDetail(name=name,email=email,subject=subject,message=message)
            contact.save()
            
            send_mail(subject,message,email,['techlifes18@gmail.com'],fail_silently=False)
            messages.success(request,'Your message has been sent. Thank you!')
        else:
            messages.warning(request,'All Fields Are Required')
    
    return render(request,'logistics/contact.html')


def quote(request):
    if request.method == "POST":
        departure = request.POST['departure']
        delivery = request.POST['delivery']
        weight = request.POST['weight']
        dimensions = request.POST['dimensions']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        if departure != "" and delivery != "" and weight != "" and dimensions != "":
            quotes = Getquotes(city_depature=departure,city_deliver=delivery,weight=weight,dimensions=dimensions,name=name,email=email,phone=phone,message=message)
            
            quotes.save()
            messages.success(request,'Thankyou will be send you the quote on mail')
        else:
            messages.warning(request,'All the Feilds Are required')
        
    return render(request,'logistics/get-a-quote.html')


def service_detail(request):
    return render(request,'logistics/service-details.html')


def cargo(request):
    return render(request,'services/cargo.html')

def logistics(request):
    return render(request,'services/logistics.html')

def packaging(request):
    return render(request,'services/packaging.html')

def trucking(request):
    return render(request,'services/trucking.html')

def warehousing(request):
    return render(request,'services/warehousing.html')

def privacy(request):
    return render(request,'logistics/privacy.html')