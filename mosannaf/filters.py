import django_filters
from .models import *


class MosannafFilter(django_filters.FilterSet):

    class Meta:
        model = Mosannaf
        fields = '__all__'
        exclude = ['image', 'file']
