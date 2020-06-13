from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render

from .serializers import ProductListSerializer, ProductDetailSerializer
from .models import Product
from .pagination import ProductPagination
from .filters import ProductFilter


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = ProductPagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('title', 'telco', 'data', 'description', 'price')
    filterset_class = ProductFilter

    def get_queryset(self):
        queryset = Product.objects.all()
        #available = self.request.query_params.get('available', None)
        # if available is not None and available == 'true':
        #    queryset = Product.objects.available_products()
        ordering = self.request.query_params.get('ordering', None)
        if ordering is not None and ordering == "max_data":
            queryset = queryset.order_by('-data') # ordering by 'most data'
        if ordering is not None and ordering == "min_price":
            queryset = queryset.order_by('price') # ordering by 'cheapest'
        if ordering is not None and ordering == "min_contract":
            queryset = queryset.order_by('contract_length') # ordering by 'shortest contract'
        # if ordering is not None and ordering == "best_seller":
        #    queryset = queryset.order_by('-sale_count')
        return queryset


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'slug'
