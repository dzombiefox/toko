# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from stok .models import Stok
from satuan .models import Satuan
class EkstrakStok(models.Model):
    stok = models.ForeignKey(Stok)
    jumlahawal = models.IntegerField()
    jumlahekstrak = models.IntegerField()
    satuan = models.ForeignKey(Satuan)
    sisa = models.IntegerField()
    keterangan =models.TextField(null=True,blank=True)
    posted_by = models.ForeignKey(User)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

# Create your models here.
