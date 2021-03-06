# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from masuk .models import Masuk
# Create your models here.
class Bhutang(models.Model):
    tanggal=models.DateField()
    penerima=models.CharField(max_length=25)
    masuk=models.ForeignKey(Masuk)
    jumlahHutang=models.IntegerField()
    jumlahBayar=models.IntegerField()
    sisaHutang=models.IntegerField()
    posted_by=models.ForeignKey(User)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)