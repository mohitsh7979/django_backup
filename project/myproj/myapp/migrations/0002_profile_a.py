# Generated by Django 4.2.1 on 2023-06-24 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='a',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
