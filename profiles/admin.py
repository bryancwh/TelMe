from django.contrib import admin

from .models import FavoritesProducts, Cluster


@admin.register(FavoritesProducts)
class FavoritesProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product')

@admin.register(Cluster)
class ClusterAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_members')