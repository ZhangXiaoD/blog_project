# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170717_0406'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='page_view',
            field=models.PositiveIntegerField(default=0),
        ),
    ]