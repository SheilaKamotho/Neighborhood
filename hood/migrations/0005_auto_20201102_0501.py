# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-02 02:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0004_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='hood_id',
            new_name='neighborhood',
        ),
    ]