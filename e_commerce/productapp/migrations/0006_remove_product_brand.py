# Generated by Django 4.1.3 on 2023-02-08 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0005_product_brand_orderplaced'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
    ]
