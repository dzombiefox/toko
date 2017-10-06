# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from bmasuk .models import Bmasuk
# Create your models here.
class Rmasuk(models.Model):
    bmasuk=models.ForeignKey(Bmasuk)
    jumlahRetur=models.IntegerField()
    keterangan=models.TextField(null=True)
    rmasukStatus=models.IntegerField(default=0,null=True,blank=True)
    posted_by=models.ForeignKey(User)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def subTotal(self):
        return int(self.jumlahRetur) * int(self.bmasuk.harga)
