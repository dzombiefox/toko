# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from stok .models import Stok


# Create your models here.

class UbahStok(models.Model):
    stok = models.ForeignKey(Stok)
    jumlah = models.IntegerField()
    stokawal = models.IntegerField()
    keterangan = models.TextField()
    posted_by = models.ForeignKey(User, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

