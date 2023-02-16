from django.urls import path
from .views import *

app_name = 'mosannaf'


urlpatterns = [
    path('', all, name='all'),
    path('details/<str:slug>', details, name='details'),
    path('query/', search, name='search'),
    path('add-rate/', add_rate, name='add-rate'),
    path('get-feedbacks/', get_feedbacks, name='get-feedbacks'),
    path('advanced-search/', advanced_search, name='advanced-search'),
    path('categories/', categories, name='categories'),
    path('categories/category/<str:slug>/', category, name='category'),
    path('categories/category/<str:category_name>/<str:sub_category>/', sub_category, name='sub-category'),
]
