# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Rmasuk
from forms import RmasukForm
from stok .models import Stok
from bmasuk .models import Bmasuk
from serializers import RmasukSerializer
from rest_framework import generics
# Create your views here.

@login_required
def index(request):
    data = Rmasuk.objects.all()
    return render(request,"rmasuk/index.html",{"data":data})

@login_required
def save(request):
    # return HttpResponse("koko")
    form=RmasukForm(request.POST)
    masuk=request.POST['bmasuk']
    bmasuk=Bmasuk.objects.get(pk=masuk)
    jumlahMasuk=request.POST['jumlahRetur']
    totalBarangMasuk =bmasuk.jumlah

    stok=Stok.objects.get(satuan=bmasuk.satuan, barang =bmasuk.barang)
    jumlahStok=stok.stok
    rmasuk=Rmasuk.objects.filter(bmasuk=bmasuk.id)

    totalRetur=0
    for data in rmasuk :
        totalRetur += data.jumlahRetur

    sisaBarang = int(totalBarangMasuk) - int(totalRetur)
    if sisaBarang <= 0 :
        return redirect(request.META['HTTP_REFERER'])
       # return HttpResponse("0")
    else:
        totalSisa = int(sisaBarang) - int(jumlahMasuk)
        if totalSisa < 0 :
            return redirect(request.META['HTTP_REFERER'])
            # return HttpResponse("1")
        else :
            form.save()
            sisaStok=jumlahStok - int(jumlahMasuk)
            stok=Stok.objects.filter(pk=stok.id).update(stok=sisaStok)
            return redirect(request.META['HTTP_REFERER'])
            # return HttpResponse("2")

    # return HttpResponse(sisaBarang)
    # form.save()

@login_required
def delete(request,id):
    #return HttpResponse("ok")
    item=Rmasuk.objects.get(pk=id)
    masuk=item.bmasuk_id


    jumlahRetur=item.jumlahRetur

    bmasuk =Bmasuk.objects.get(id=masuk)
    # return HttpResponse("oko")
    masukId=bmasuk.id
    satuanId=bmasuk.satuan
    barangId=bmasuk.barang

    stok=Stok.objects.get(barang=barangId,satuan=satuanId)
    jumlahStok=stok.stok
    totalStok =int(jumlahStok) + int(jumlahRetur)
    Stok.objects.filter(pk=stok.id).update(stok=totalStok)
    # return HttpResponse(jumlahStok)


    item.delete()
    return redirect(request.META['HTTP_REFERER'])


class GetReturJson(generics.ListAPIView):
    serializer_class = RmasukSerializer
    def get_queryset(self):
        id=self.kwargs['id']
        return Rmasuk.objects.filter(bmasuk__masuk=id)

