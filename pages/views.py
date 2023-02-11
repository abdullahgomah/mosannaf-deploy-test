from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import * 
from mosannaf.models import Branch, Mosannaf


def index(request):
    """
    تعتمد أقسام الكتب الظاهرة في الصفحة الرئيسية على قاعدة بيانات 
    الأقسام في تطبيق "مصنف" .... 
    حقل "عرض في الصفحة الرئيسية" .. 
    في حالة الحقل "نعم" يتم العرض والعكس
    """
    categories = Branch.objects.filter(view_in_home__exact=True)
    mosannafs = Mosannaf.objects.all() 
    content = Home.objects.last()
    context = {
        'categories': categories, 
        'content': content,
        'mosannafs': mosannafs,
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


@login_required
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


## handle errors 

def handel404(request, exception):
    return render(request, '404.html', status=404)
