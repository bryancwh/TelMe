# Generated by Django 2.2.10 on 2020-06-24 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    
    dependencies = [
        ('products', '0005_auto_20200613_0718'),
        ('profiles', '0007_cluster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favoritesproducts',
            name='products',
        ),
        migrations.AddField(
            model_name='favoritesproducts',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
        migrations.AlterField(
            model_name='favoritesproducts',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
