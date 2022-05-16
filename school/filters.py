from dataclasses import fields
import imp
import django_filters

from .models  import *

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Lietotaji
        fields = '__all__'
