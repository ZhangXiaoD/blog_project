# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170717_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='last_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
