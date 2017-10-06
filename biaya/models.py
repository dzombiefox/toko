# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from masuk .models import Masuk

# Create your models here.
class Biaya(models.Model):
    masuk=models.ForeignKey(Masuk)
    namaBiaya=models.CharField(max_length=100,verbose_name="NAMA BIAYA")
    jumlahBiaya=models.CharField(max_length=15)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

