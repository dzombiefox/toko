# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-28 10:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rmasuk', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rmasuk',
            old_name='user',
            new_name='posted_by',
        ),
    ]
