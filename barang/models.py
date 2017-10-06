# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from kategori .models import Kategori


#Create your models here.
class Barang(models.Model):
    kodeBarang=models.CharField(max_length=15,verbose_name="KODE BARANG")
    namaBarang=models.CharField(max_length=45,verbose_name="NAMA BARANG")
    kategory=models.ForeignKey(Kategori,verbose_name="KATEGORI")
    posted_by=models.ForeignKey(User,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return  self.namaBarang

