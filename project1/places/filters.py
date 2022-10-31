import django_filters
from .models import Place

class PlaceFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Place
        fields = ['title']
