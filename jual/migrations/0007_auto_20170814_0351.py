# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-14 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jual', '0006_auto_20170808_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jual',
            name='pembayaran',
            field=models.CharField(blank=True, choices=[('0', 'HUTANG'), ('1', 'LUNAS')], default=0, max_length=6, null=True),
        ),
    ]
