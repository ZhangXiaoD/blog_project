# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 19:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='creat_time',
            new_name='create_time',
        ),
    ]