# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from masuk .models import Masuk
from barang .models import Barang
from satuan .models import Satuan
# Create your models here.
class Bmasuk(models.Model):
    masuk=models.ForeignKey(Masuk)
    barang=models.ForeignKey(Barang)
    satuan=models.ForeignKey(Satuan)
    jumlah=models.IntegerField()
    harga=models.CharField(max_length=12)
    posted_by = models.ForeignKey(User)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def subtotal(self):
        return int(self.harga) * self.jumlah