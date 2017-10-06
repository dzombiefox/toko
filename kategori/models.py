# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Kategori(models.Model):
    namaKategori= models.CharField(max_length=25, verbose_name="NAMA KATEGORI")
    posted_by = models.ForeignKey(User,null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.namaKategori

