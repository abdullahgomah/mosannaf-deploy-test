from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from .models import *


def index(request):
    content = Home.objects.last()
    context = {
        'content': content,
    }
    return render(request, 'pages/index.html', context)


def contact(request):
    content = Home.objects.last()
    if request.POST:
        email = request.POST.get('email')
        details = request.POST.get('details')
        if details == '':
            messages.add_message(request, messages.ERROR,
                                 'الرجاء ملء جميع الحقول')
        else:
            Message.objects.create(email=email, details=details)
            messages.add_message(request, messages.SUCCESS,
                                 "تم إرسال رسالتك وسيتم التواصل معك قريباً")
    contact_info = Contact.objects.last()
    context = {
        'contact': contact_info
    }
    return render(request, 'pages/contact.html', context)


def suggest(request):
    content = Home.objects.last()
    if request.POST:
        details = request.POST.get('details')
        if details == '':
            messages.add_message(request, messages.ERROR,
                                 "الرجاء ملء جميع الحقول")
        else:
            Suggestion.objects.create(details=details)
            messages.add_message(request, messages.SUCCESS,
                                 "تم إرسال ترشيحك وسيتم إضافته قريباً")
    context = {
        'content': content,
    }
    return render(request, 'pages/suggest.html', context)
