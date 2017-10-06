# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-20 03:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suplier', '0002_auto_20170719_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suplier',
            name='alamatToko',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='suplier',
            name='posted_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]