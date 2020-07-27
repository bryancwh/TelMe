from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

from accounts.serializers import UserSerializer
from .models import FavoritesProducts, Cluster
from products.models import Product
from products.serializers import ProductListSerializer, ProductDetailSerializer

#Needs merge with above
from django.http import HttpResponseRedirect
from django.urls import reverse
from .suggestions import update_clusters

import datetime

from django.contrib.auth.decorators import login_required

User = get_user_model()


class UserView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class FavoritesProductsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user

        #super inefficient way of querying lol
        helper = []
        qs = FavoritesProducts.objects.filter(user=user)
        for i in qs:
            helper.append(i.product)
        
        products = ProductListSerializer(
            helper, context={'request': request}, many=True).data
        return Response(products)


class UpdateFavoritesProductsView(APIView):
    """Get product then if product in favorites products exists remove from that, 
    else add it to favorites products"""

    permission_classes = (IsAuthenticated,)

    def already_favorited_product(user, product_id):
        product = Product.objects.get(id=product_id)
        return FavoritesProducts.objects.filter(user=user, product=product).exists()

    def post(self, request, id):
        user = request.user
        product = get_object_or_404(Product, id=id)

        if not FavoritesProducts.objects.filter(user=user, product=product).exists():
            FavoritesProducts.objects.create(user=request.user, product=product)
        else:
            FavoritesProducts.objects.filter(user=request.user, product=product).delete()

        try:
            update_clusters()
        except:
            pass

        product = ProductListSerializer(
            product, context={'request': request})
        return Response(product.data)


class RecommendedProductsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        user=request.user

        # get request user favorited products
        user_favorite_products = FavoritesProducts.objects.filter(user=user).prefetch_related('product')
        user_favorite_products_ids = set(map(lambda x: x.product.id, user_favorite_products))
        
        # get request user cluster name (just the first one right now)
        try:
            user_cluster_name = \
                User.objects.get(email=user.email).cluster_set.first().name
        except: # if no cluster assigned for a user, update clusters
            update_clusters()
            user_cluster_name = \
                User.objects.get(email=user.email).cluster_set.first().name
        
        # get usernames for other memebers of the cluster
        user_cluster_other_members = \
            Cluster.objects.get(name=user_cluster_name).users \
                .exclude(email=user.email).all()
        #other_members_usernames = set(map(lambda x: x.username, user_cluster_other_members))

        # get favorited products by those users, excluding request user's favorite products
        other_users_favorite_products = \
            FavoritesProducts.objects.filter(user__in=user_cluster_other_members) \
                .exclude(product__id__in=user_favorite_products_ids)
        other_users_favorite_products_ids = set(map(lambda x: x.product.id, other_users_favorite_products))
        
        # then get a products list including the previous IDs, order by rating
        product_list = list(Product.objects.filter(id__in=other_users_favorite_products_ids))
        
        products = ProductListSerializer(
            product_list, context={'request': request}, many=True).data
        return Response(products)


#Non-API Version:
#@login_required
#def user_recommendation_list(request):
    
    # get request user favorited products
#    user_favorite_products = FavoritesProducts.objects.filter(user_name=request.user.username).prefetch_related('product')
#    user_favorite_products_ids = set(map(lambda x: x.product.id, user_favorite_products))

    # get request user cluster name (just the first one righ now)
#    try:
#        user_cluster_name = \
#            User.objects.get(username=request.user.username).cluster_set.first().name
#    except: # if no cluster assigned for a user, update clusters
#        update_clusters()
#        user_cluster_name = \
#            User.objects.get(username=request.user.username).cluster_set.first().name
    
    # get usernames for other memebers of the cluster
#    user_cluster_other_members = \
#        Cluster.objects.get(name=user_cluster_name).users \
#            .exclude(username=request.user.username).all()
#    other_members_usernames = set(map(lambda x: x.username, user_cluster_other_members))

    # get favorited products by those users, excluding request user's favorite products
#    other_users_favorite_products = \
#        FavoritesProducts.objects.filter(user_name__in=other_members_usernames) \
#            .exclude(product__id__in=user_favorite_products_ids)
#    other_users_favorite_products_ids = set(map(lambda x: x.product.id, other_users_favorite_products))
    
    # then get a products list including the previous IDs, order by rating
#    product_list = sorted(
#        list(Product.objects.filter(id__in=other_users_favorite_products_ids)), 
#        key=lambda x: x.average_rating, 
#        reverse=True
#    )

    #needs editing
#    return render(
#        request, 
#        'favorite_products/user_recommendation_list.html', 
#        {'username': request.user.username,'product_list': product_list}
#    )