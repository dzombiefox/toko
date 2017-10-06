# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from .forms import RjualForm
from .models import Rjual
from bjual .models import Bjual
from django.shortcuts import render,redirect
from django.contrib import messages
from stok .models import Stok
# Create your views here.
from serializers import RjualSerializer
from rest_framework import generics
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    data = Rjual.objects.all()
    return render(request,"rjual/index.html",{"data":data})

def save(request):
    # return HttpResponse("dsad")
    data = RjualForm(request.POST)
    jumlah=request.POST['jumlah']
    bjual=request.POST['bjual']
    dat=Bjual.objects.get(pk=bjual)
    jumlahJual=int(dat.jumlahJual) - int(jumlah)
    pilihan = request.POST['pilihan']
    if jumlahJual <0 :
       return redirect(request.META['HTTP_REFERER'],
                        messages.add_message(request, messages.INFO, 'Maaf jumlah bayar tidak boleh melebihi hutang'))
    else :
        stok = Stok.objects.get(barang=dat.barang, satuan=dat.satuan)
        jumlahStok=int(stok.stok) + int (jumlah)
        if pilihan == "0":
            Stok.objects.filter(pk=stok.id).update(stok=jumlahStok)
            Bjual.objects.filter(pk=dat.id).update(jumlahJual=jumlahJual)
            data.save()
            return redirect(request.META['HTTP_REFERER'],
                   messages.add_message(request, messages.INFO, 'Maaf jumlah bayar tidak boleh melebihi hutang'))
        else :
            Bjual.objects.filter(pk=dat.id).update(jumlahJual=jumlahJual)
            data.save()
            return redirect(request.META['HTTP_REFERER'],
                            messages.add_message(request, messages.INFO,
                                                 'Maaf jumlah bayar tidak boleh melebihi hutang'))

def delete(request,id):
    # return  HttpResponse("jiw")
    item=Rjual.objects.get(pk=id)
    bjual=Bjual.objects.get(pk=item.bjual_id)
    pilihan=item.pilihan
    barang=bjual.barang
    satuan=bjual.satuan
    jumlah=item.jumlah

    jumlahJual=int(bjual.jumlahJual) + int (jumlah)
    Bjual.objects.filter(pk=bjual.id).update(jumlahJual=jumlahJual)


    # if pilihan == "0" :
    stok = Stok.objects.get(barang=barang, satuan=satuan)
    jumlahStok = stok.stok

    pilihan = item.pilihan
    if pilihan == "1" :
        # totalStok = int(jumlahStok) + int(jumlah)
        # Stok.objects.filter(pk=stok.id).update(stok=totalStok)
        item.delete()
        return redirect(request.META['HTTP_REFERER'])

    else :
        totalStok = int(jumlahStok) - int(jumlah)
        Stok.objects.filter(pk=stok.id).update(stok=totalStok)
        item.delete()
        return redirect(request.META['HTTP_REFERER'])




class GetRjualJson(generics.ListAPIView):
    serializer_class = RjualSerializer
    def get_queryset(self):
        id=self.kwargs['id']
        return Rjual.objects.filter(bjual__jual=id)

