from django.db import models
from autoslug import AutoSlugField
from web.utils import id_generator

class ProductManager(models.Manager):
    def all(self):
        return self.filter(active=True)

    #def available_products(self):
    #    return self.all().filter(sizes__available_count__gt=0).distinct()


class Product(models.Model):
    CATEGORY = (
        ('Postpaid', 'Postpaid'),
        ('Prepaid', 'Prepaid'),
        ('Pay-as-you-go', 'Pay-as-you-go'),
    )

    TELCO = (
        ('Singtel', 'Singtel'),
        ('Starhub', 'Starhub'),
        ('M1', 'M1'),
        ('Circles.Life', 'Circles.Life'),
        ('CMLink', 'CMLink'),
        ('MyRepublic', 'MyRepublic'),
        ('giga!', 'giga!'),
        ('redONE', 'redONE'),
        ('GOMO', 'GOMO'),
        ('Zero1', 'Zero1'),
        ('VIVIFI', 'VIVIFI'),
        ('TPG Mobile', 'TPG Mobile'),
        ('Grid Mobile', 'GridMobile'),
    )

    title = models.CharField(max_length=120)
    slug = AutoSlugField(populate_from='title',
                         unique_with=['title'], unique=True)
    telco = models.CharField(max_length=200, null=True, choices=TELCO)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.IntegerField()
    call_time = models.IntegerField()
    sms = models.IntegerField()
    contract_length = models.DecimalField(max_digits=10, decimal_places=1)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    #discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #sizes = models.ManyToManyField(Size)
    #colors = models.ManyToManyField('self', blank=True, related_name='colors')
    #sale_count = models.IntegerField(default=0)
    #code = models.CharField(max_length=40, unique=True, editable=False)

    #objects = ProductManager()

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.code = id_generator()
        super(Product, self).save(*args, **kwargs)

    #@property
    #def available(self):
    #    return self.active()

    #@property
    #def discount_percent(self):
    #    if self.discount_price:
    #        discount_percent = 100 - (self.discount_price * 100) / self.price
    #        return int(discount_percent)
    #    return

    #@property
    #def final_price(self):
    #    if self.discount_price:
    #        return self.discount_price
    #    return self.price

    #@property
    #def customer_profit(self):
    #    if self.discount_price:
    #        return self.price - self.discount_price
    #    return 0
