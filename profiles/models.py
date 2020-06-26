from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

from products.models import Product

User = get_user_model()

class FavoritesProductsManager(models.Manager):
    def check_product(self, user, product):
        if user.is_authenticated:
            return FavoritesProducts.objects.filter(user=user, product=product).exists()


class FavoritesProducts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)

    objects = FavoritesProductsManager()

    class Meta:
        verbose_name_plural = 'Favorites Products'

    def __str__(self):
        return self.user.username

#Old version:
#@receiver(post_save, sender=User)
#def create_favorite_products(sender, instance, created, **kwargs):
#    if created:
#        FavoritesProducts.objects.create(user=instance)


#@receiver(post_save, sender=User)
#def save_favorite_products(sender, instance, **kwargs):
#    instance.favorite_products.save()


class Cluster(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

    def get_members(self):
        return "\n".join([u.username for u in self.users.all()])