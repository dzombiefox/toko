# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Jual(models.Model):
    statusBeli = (
        ('0', 'LANGGANAN'),
        ('1', 'BUKAN LANGGANAN'),

    )
    methode = (
        ('0', 'HUTANG'),
        ('1', 'LUNAS'),

    )
    tanggal=models.DateField(null=True,blank=True)
    namaPembeli=models.CharField(max_length=50,verbose_name="NAMA PEMBELI",null=True,blank=True)
    statusPembeli=models.CharField(max_length=6,choices=statusBeli,default='0',null=True,blank=True)
    pembayaran=models.CharField(max_length=6,choices=methode,null=True,blank=True,default=0)
    potongan=models.CharField(max_length=8,blank=True,null=True,default=0)
    bayar = models.CharField(max_length=8, blank=True, null=True,default=0)
    keterangan=models.CharField(max_length=250,null=True,blank=True)
    posted_by = models.ForeignKey(User,null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.namaPembeli)


