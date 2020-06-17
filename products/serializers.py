from rest_framework import serializers

from .models import Product
from profiles.models import FavoritesProducts

class ProductListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Product
        fields = ('id', 'slug', 'url', 'title', 'telco',
                  'category', 'price', 'data', 'call_time',
                  'sms', 'contract_length', 'description')


class ProductDetailSerializer(serializers.ModelSerializer):
    is_favorite_product = serializers.SerializerMethodField()
    #discount_percent = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    #def get_default_size(self, obj):
    #    sizes = obj.sizes.available_sizes()
    #    if not sizes.exists():
    #        return
    #    return sizes.first().id

    #def get_available(self, obj):
    #    return obj.available

    #def get_discount_percent(self, obj):
    #    return obj.discount_percent

    def get_is_favorite_product(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            return FavoritesProducts.objects.check_product(user, obj.id)
        return False

    #def get_is_in_cart(self, obj):
    #    user = self.context.get('request').user
    #    if user.is_authenticated:
    #        return user.carts.get(ordered=False).items.filter(product=obj.id).exists()
    #    return False
