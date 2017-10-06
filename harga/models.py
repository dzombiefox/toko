# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from barang .models import Barang
from  satuan .models import Satuan
# Create your models here.

class Harga(models.Model):
    barang=models.ForeignKey(Barang,verbose_name="BARANG")
    satuan=models.ForeignKey(Satuan,verbose_name="SATUAN")
    modal=models.CharField(max_length=15,verbose_name="HARGA MODAL")
    jual = models.CharField(max_length=15, verbose_name="HARGA JUAL")
    posted_by = models.ForeignKey(User)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
