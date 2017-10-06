# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from bjual .models import Bjual

# Create your models here.

class Rjual(models.Model):
    choice = (
        ('0', 'KEMBALI KE STOK'),
        ('1', 'MUSNAHKAN BARANG'),

    )
    bjual =models.ForeignKey(Bjual)
    jumlah=models.IntegerField()
    pilihan=models.CharField(choices=choice,default='0',max_length=15)
    keterangan=models.TextField(null=True)
    posted_by = models.ForeignKey(User)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)



