

import django_filters
from .models import*


class OrderFilters(django_filters.FiletersSet):
    class Meta:
        model = Game
        fields = '__all__'
 