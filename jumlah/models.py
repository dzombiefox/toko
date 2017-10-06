# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from barang .models import Barang
from satuan .models import Satuan
from django.db import models

# Create your models here.

class Jumlah(models.Model):
    barang=models.ForeignKey(Barang,verbose_name="BARANG")
    satuanBesar=models.ForeignKey(Satuan,verbose_name="SATUAN BESAR",related_name="satuan_besar")
    satuanKecil=models.ForeignKey(Satuan,verbose_name="SATUAN KECIL",related_name="satuan_kecil")
    jumlah=models.CharField(max_length=15, verbose_name="JUMLAH")
    posted_by = models.ForeignKey(User,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     if Jumlah.objects.filter(self.barang).exists() and Jumlah.objects.filter(self.satuanBesar).exists() and Jumlah.objects.filter(self.satuanKecil).exists():
    #         return  "data sudah ada"
    #     else:
    #         super(Jumlah,self).save(*args,**kwargs)
