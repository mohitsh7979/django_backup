# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-22 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeldb", "0014_auto_20170323_1106"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobalert",
            name="is_unsubscribe",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="jobalert",
            name="unsubscribe_code",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="subscriber",
            name="is_unsubscribe",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="subscriber",
            name="unsubscribe_code",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
