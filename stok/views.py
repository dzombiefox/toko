# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Stok
from forms import StokForm
from ubahstok .forms import UbahStokForm
from functions .functions import decript
from  ekstrakstok .forms import FormEkstrakStok
from serializers import StokSerializer
from rest_framework import generics
def index(request):
    data = Stok.objects.all()
    form = StokForm()
    frm  = UbahStokForm
    fr =FormEkstrakStok
    return render(request , "stok/index.html",{"data":data,"form":form,"frm":frm,"fr":fr})

class GetStokJson(generics.ListAPIView):
    serializer_class = StokSerializer
    def get_queryset(self):
        id=self.kwargs['id']
        return Stok.objects.filter(barang=id)
