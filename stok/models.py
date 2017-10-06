# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from satuan .models import Satuan
from barang .models import Barang
# Create your models here.
class Stok(models.Model):
    satuan=models.ForeignKey(Satuan)
    barang=models.ForeignKey(Barang)
    stok=models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)