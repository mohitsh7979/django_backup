# Generated by Django 4.2.5 on 2023-09-09 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_1', '0003_myprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofile',
            name='image',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]