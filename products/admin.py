from django.contrib import admin

from .models import Product

#To import and export data from admin
from import_export.admin import ImportExportModelAdmin

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('id', 'title', 'telco', 'category', 'price', 'data', 'call_time', 'sms', 'contract_length', 'description', 'created_at', 'created_at')
    list_display_links = ('id', 'title')
    list_filter = ('created_at',)
    list_per_page = 25
    search_fields = ('title', 'telco', 'data', 'description', 'price')