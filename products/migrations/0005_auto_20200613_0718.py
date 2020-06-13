# Generated by Django 2.2.10 on 2020-06-13 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200613_0713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='monthly_bill',
            new_name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='call_time',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
    ]