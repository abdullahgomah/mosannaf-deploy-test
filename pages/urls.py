from django.urls import path
from .views import *

app_name = 'pages'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('suggest/', suggest, name='suggest'),
]
