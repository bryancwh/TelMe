from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('id', 'title', 'price',
                     'active', 'created_at')
    list_display_links = ('id', 'title')
    list_editable = ('active',)
    list_filter = ('active', 'created_at')
    list_per_page = 25
    search_fields = ('title', 'price', 'description')