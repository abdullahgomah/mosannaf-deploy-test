from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import * 
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json 

# Create your views here.


def all(request):
    mosannafs = Mosannaf.objects.all().order_by('-date_published')

    context ={
        'mosannafs': mosannafs, 
    } 

    return render(request, 'mosannaf/all.html', context)
    


def details(request, id):
    mosannaf = Mosannaf.objects.get(id=id)
    form = RateForm() 
    form1 = AddRate() 
    rates = Rate.objects.filter(mosannaf=mosannaf) 
    
    context = {
        'mosannaf': mosannaf,
        'rates': rates, 
        'form': form, 
        'form1': form1, 
    }

    return render(request, 'mosannaf/mosannaf_details.html', context)


def search(request): 
    search_input = request.GET['search_input'] 
    if search_input != "":
        # show message here
        results = Mosannaf.objects.filter(name__contains=search_input)
        
    else:
        messages.add_message(request, messages.ERROR,'الحقل فارغ! الرجاء كتابة كلمة البحث ')
        results = "" 
    
    context = {
        'results': results,
        'search_word': request.GET['search_input'],
    } 

    return render(request, 'mosannaf/search_results.html', context)

def add_rate(request):
    if request.POST.get('action') == 'post':
        details = request.POST.get('details')  
        id = int(request.POST.get('mosannaf_id')) 
        mosannaf = get_object_or_404(Mosannaf, id=id)

        Rate.objects.create(mosannaf=mosannaf, details=details)


        return JsonResponse({'feedbacks': serializers.serialize('json', Rate.objects.filter(mosannaf = mosannaf))})

        
    

def get_feedbacks(request):
    if request.GET: 
        mosannaf_id = request.GET.get('mosannaf_id')
        feedbacks = Rate.objects.filter(mosannaf=get_object_or_404(Mosannaf, id=mosannaf_id))
        # print(mosannaf_id) 
        # print(feedbacks) 
        # return JsonResponse({'feedbacks': serializers.serialize('json', feedbacks)})
    context ={
        'feedbacks':feedbacks,
    }
    return render(request, 'mosannaf/feedbacks.html', context)