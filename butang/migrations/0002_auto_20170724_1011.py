# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-24 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('butang', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='butang',
            name='sisaHutang',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
