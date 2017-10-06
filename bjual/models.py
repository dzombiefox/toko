# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from jual .models import Jual
from barang .models import Barang
from satuan .models import Satuan

# Create your models here.

class Bjual(models.Model):
    jual=models.ForeignKey(Jual)
    barang=models.ForeignKey(Barang)
    satuan=models.ForeignKey(Satuan)
    hargaModal=models.CharField(max_length=15)
    hargaJual=models.CharField(max_length=15)
    jumlahJual=models.IntegerField()
    hargalain=models.CharField(max_length=12,null=True,blank=True,default=0)
    pilihan=models.CharField(max_length=15)

    def subtotal(self):
        return int(self.hargaJual) * int(self.jumlahJual)

    def total(self):
        data=0
        data += int(self.hargaJual) * int(self.jumlahJual)
        return data

    def kacrut(self):
        return 1

    def selisih(self):
        return  int(self.jumlahJual) * ( int(self.hargaJual) - (int(self.hargaModal)))