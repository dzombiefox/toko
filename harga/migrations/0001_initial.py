# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-18 02:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('barang', '0001_initial'),
        ('satuan', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Harga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modal', models.CharField(max_length=15, verbose_name='HARGA MODAL')),
                ('jual', models.CharField(max_length=15, verbose_name='HARGA JUAL')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('barang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barang.Barang', verbose_name='BARANG')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('satuan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='satuan.Satuan', verbose_name='SATUAN')),
            ],
        ),
    ]
