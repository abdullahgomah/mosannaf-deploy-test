from django.urls import path
from .views import *

app_name = 'mosannaf'


urlpatterns = [
    path('', all, name='all'),
    path('details/<int:id>', details, name='details'),
    path('query/', search, name='search'),
    path('add-rate/', add_rate, name='add-rate'),
    path('get-feedbacks/', get_feedbacks, name='get-feedbacks'),
    path('advanced-search/', advanced_search, name='advanced-search'),
    path('del-rate/<int:id>/', del_rate, name='del-rate')
]
