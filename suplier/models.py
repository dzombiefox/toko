# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Suplier(models.Model):
    stat = (
        ('0', 'AKTIF'),
        ('1', 'TIDAK AKTIF'),

    )
    namaSuplier=models.CharField(max_length=15, verbose_name="NAMA SUPLIER")
    namaToko = models.CharField(max_length=115, verbose_name="NAMA TOKO")
    alamatToko = models.TextField(blank=True)
    status=status=models.CharField(max_length=6,choices=stat,default='0')
    posted_by = models.ForeignKey(User,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.namaSuplier
