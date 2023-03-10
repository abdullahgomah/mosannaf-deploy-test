from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import *
from .forms import *
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
from .filters import MosannafFilter
from django.contrib.auth.decorators import login_required
from pages.models import Home


# Create your views here.


def all(request):
    mosannafs = Mosannaf.objects.all().order_by('-date_published')
    content = Home.objects.last()

    context = {
        'mosannafs': mosannafs,
        'content': content, 
    }

    return render(request, 'mosannaf/all.html', context)

def all_translated(request): 
    '''
    THIS is gets all mosannafs from TranslatedMosannaf model
    '''
    mosannafs = TranslatedMosannaf.objects.all().order_by("-date-published") 
    content = Home.objects.last() 

    context = {

    }

    return render(request, 'mosannaf/all.html', context) 

def details(request, slug):
    mosannaf = Mosannaf.objects.get(slug=slug)
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
        messages.add_message(request, messages.ERROR,
                             'الحقل فارغ! الرجاء كتابة كلمة البحث ')
        results = ""

    context = {
        'results': results,
        'search_word': request.GET['search_input'],
    }

    return render(request, 'mosannaf/search_results.html', context)

@login_required
def add_rate(request):

    if request.POST.get('action') == 'post':
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
            
        details = request.POST.get('details')
        score = request.POST.get('score')
        id = int(request.POST.get('mosannaf_id'))
        mosannaf = get_object_or_404(Mosannaf, id=id)

        Rate.objects.create(user=request.user, mosannaf=mosannaf, details=details, score=score)

        return JsonResponse({'feedbacks': serializers.serialize('json', Rate.objects.filter(mosannaf=mosannaf))})


def get_feedbacks(request):
    if request.GET:
        mosannaf_id = request.GET.get('mosannaf_id')
        feedbacks = Rate.objects.filter(
            mosannaf=get_object_or_404(Mosannaf, id=mosannaf_id))
        # print(mosannaf_id)
        # print(feedbacks)
        # return JsonResponse({'feedbacks': serializers.serialize('json', feedbacks)})
    context = {
        'feedbacks': feedbacks,
    }
    return render(request, 'mosannaf/feedbacks.html', context)


def advanced_search(request):

    mosannafs = Mosannaf.objects.all()

    mosannaf_filter = MosannafFilter(
        request.GET, queryset=mosannafs)  # mosannaf filter form

    results = mosannaf_filter.qs

    context = {
        'mosannaf_filter': mosannaf_filter,
        'results': results,
    }
    return render(request, 'mosannaf/advanced-search.html', context)


# categories
def categories(request):
    categories = Branch.objects.all() 
    content = Home.objects.last()
    context = {
        'categories': categories,
        'content': content, 
    }
    return render(request, 'mosannaf/categories.html', context)


def category(request, slug):
    """
    THIS function take an objects from Branch model and SubBranch Model 
    هذه دالة القسم الواحدة وتحتوي على المصنفات التي تخص القسم كما تحتوي على الأقسام الفرعبة لهذا القسم
    """
    category= Branch.objects.get(slug=slug)
    print(category)
    sub_categories = SubBranch.objects.filter(branch=category)
    mosannafs = Mosannaf.objects.filter(branch=category)

    # print(mosannafs)

    context = {
        'category_title': category,
        'sub_categories': sub_categories, 
        'mosannafs': mosannafs
    }
    return render(request, 'mosannaf/category.html', context)


def sub_category(request, category_name, sub_category):
    """
    دالة الأقسام الفرعية
    تحتوي على الأقسام الفرعية التي تندرج تحت قسم معين كما تحوي الكتب التي تخص هذا القسم فقط
    Sub Category Function
    It contains sub categories < category, it also contains books for this category (Branch) 
    """
    category= SubBranch.objects.get(slug=sub_category)
    mosannafs = Mosannaf.objects.filter(sub_branch__name=sub_category)
    
    print(category)

    context = {
        'category': category, 
        'mosannafs': mosannafs
    }
    return render(request, 'mosannaf/category.html', context)