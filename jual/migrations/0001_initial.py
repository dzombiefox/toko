# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-18 04:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Jual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField()),
                ('namaPembeli', models.CharField(max_length=50, verbose_name='NAMA PEMBELI')),
                ('statusPembeli', models.CharField(choices=[('0', 'LANGGANAN'), ('1', 'BUKAN LANGGANAN')], default='0', max_length=6)),
                ('pembayaran', models.CharField(choices=[('0', 'HUTANG'), ('1', 'LUNAS')], default='1', max_length=6)),
                ('potongan', models.CharField(max_length=15)),
                ('keterangan', models.TextField(null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
