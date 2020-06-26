from rest_framework import serializers

from .models import Product
from profiles.models import FavoritesProducts


class ProductListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='slug'
    )
    is_favorite_product = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_is_favorite_product(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            return FavoritesProducts.objects.check_product(user, obj)
        else:
            return False
        


class ProductDetailSerializer(serializers.ModelSerializer):
    is_favorite_product = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_is_favorite_product(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            return FavoritesProducts.objects.check_product(user, obj)
        return False
