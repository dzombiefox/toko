# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-17 15:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('satuan', '0002_auto_20170720_0310'),
        ('ekstrakstok', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ekstrakstok',
            name='satuan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='satuan.Satuan'),
            preserve_default=False,
        ),
    ]