from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from models import UbahStok
from stok .models import Stok
from django.contrib.auth.models import User
from barang .models import Barang
from satuan .models import Satuan
from jual .models import Jual

from rest_framework import generics
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

@login_required
def index(request):
    data = UbahStok.objects.all()
    return render(request,"ubahstok/index.html",{"data":data})

@login_required
def save(request):
    # return HttpResponse("oo")
    id= request.POST["stok"]
    keterangan = request.POST['keterangan']
    jumlah = request.POST['jumlah']
    stok = Stok.objects.get(id=id)
    jumlahstok = stok.stok
    posted_by = request.POST['posted_by']
    ubahstok = UbahStok(stok_id = id,jumlah = jumlah,stokawal = jumlahstok,keterangan = keterangan,posted_by_id = posted_by )
    ubahstok.save()
    Stok.objects.filter(pk=id).update(stok = jumlah)
    return redirect(request.META['HTTP_REFERER'])