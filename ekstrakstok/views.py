# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import  FormEkstrakStok
from jumlah .models import Jumlah
from ekstrakstok .models import EkstrakStok
from stok .models import Stok
from functions .functions import decript

# Create your views here.

@login_required
def index(request):
    data = EkstrakStok.objects.all()
    return render(request,"ekstrakstok/index.html",{"data":data})

@login_required
def save(request):
    stok = request.POST['stok']
    jumlahawal = request.POST['jumlahawal']
    jumlahubah = request.POST['jumlahekstrak']
    sisa = int (jumlahawal) - int (jumlahubah)
    satuankecil = request.POST['satuan']
    keterangan = request.POST['keterangan']
    datastok = Stok.objects.get(pk = stok)
    barang = datastok.barang

    satuanbesar = datastok.satuan
    posted_by =request.POST['posted_by']

    # return HttpResponse(satuanbesar)
    cekjumlah = Jumlah.objects.filter(barang = barang,satuanBesar=satuanbesar,satuanKecil_id=satuankecil)

    if cekjumlah.exists() :
        # return HttpResponse("21wwd")
        getjumlah = Jumlah.objects.get(barang = barang,satuanBesar=satuanbesar,satuanKecil_id=satuankecil)

        jumlahnya = getjumlah.jumlah

        totaljumlah = int (jumlahubah) * int (jumlahnya)

        # return HttpResponse(totaljumlah)
        sisajumlah = int(jumlahawal) - int (jumlahubah)
        cekstok = Stok.objects.filter(barang = datastok.barang,satuan_id = satuankecil)

        if cekstok.exists():
            # return HttpResponse("coco")
            Stok.objects.filter(pk=stok).update(stok=sisajumlah)
            getStok = Stok.objects.get(barang = datastok.barang,satuan_id = satuankecil)
            stoknya = getStok.stok
            stokakhir = int (stoknya) + int (totaljumlah)
            Stok.objects.filter(pk=getStok.id).update(stok = stokakhir)
            dataekstrak = EkstrakStok(stok_id = stok ,jumlahawal = jumlahawal,jumlahekstrak=jumlahubah,posted_by_id=posted_by,satuan_id=satuankecil,sisa = sisa)
            dataekstrak.save()
            # Stok.objects.filter(barang = datastok.barang,satuan_id = satuankecil).update()
            return HttpResponse("1")
        else :
            Stok.objects.filter(pk=stok).update(stok = sisajumlah)
            baru = Stok(barang = datastok.barang,satuan_id=satuankecil,stok = totaljumlah)
            baru.save()
            dataekstrak = EkstrakStok(stok_id=stok, jumlahawal=jumlahawal, jumlahekstrak=jumlahubah,
                                      posted_by_id=posted_by, satuan_id=satuankecil,sisa = sisa)
            dataekstrak.save()
            return HttpResponse("1")

    else :
        return HttpResponse("0")



    # return HttpResponse(request.POST['jumlahawal'])
    # if request.POST :
    #  ekstrak = FormEkstrakStok(request.POST)
    #  if ekstrak.is_valid():
    #      ekstrak.save()
    #      return HttpResponse("ok")
    #  else :
    #      return HttpResponse(ekstrak)
    #  return HttpResponse("cocok")
    # else :
    #     return HttpResponse("sia ")