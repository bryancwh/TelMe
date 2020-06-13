from django_filters.rest_framework import FilterSet, NumberFilter
from .models import Product


class ProductFilter(FilterSet):
    min_price = NumberFilter(field_name="price", lookup_expr='gte')
    max_price = NumberFilter(field_name="price", lookup_expr='lte')
    min_data = NumberFilter(field_name="data", lookup_expr='gte')
    max_data = NumberFilter(field_name="data", lookup_expr='lte')
    min_contract = NumberFilter(field_name="contract_length", lookup_expr='gte')
    max_contract = NumberFilter(field_name="contract_length", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'min_data', 'max_data', 'min_contract', 'max_contract', 'call_time', 'sms', 'telco', 'category']
