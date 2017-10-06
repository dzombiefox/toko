# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Jumlah
from forms import JumlahForm
from functions .functions import decript
# Create your views here.

@login_required
def index(request):
    data=Jumlah.objects.all()
    return render(request,"jumlah/index.html",{"jumlah":data})

@login_required
def add(request):
    form=JumlahForm()
    return render(request, "jumlah/add.html", {"form": form})

@login_required
def save(request):
    form = JumlahForm(request.POST)
    if form.is_valid():
        c = form.save(commit=False)
        barang = c.barang
        satuanbesar = c.satuanBesar
        satuankecil = c.satuanKecil
        # return HttpResponse("kokw")
        cekjumlah = Jumlah.objects.filter(barang=barang,satuanBesar=satuanbesar,satuanKecil=satuankecil)
        if cekjumlah.exists():
            return HttpResponse("0")
        else :
            form.save()
            return HttpResponse("1")
    else:
        return HttpResponse("form failed")
    # if form.is_valid():
    #     if form.save():
    #       return HttpResponse("Berhasil Menambah Data")
    #     else:
    #       return  HttpResponse("No oke")
    # else:
    #     return HttpResponse("form failed")

@login_required
def edit(request,data):
    id=decript(data)
    data=Jumlah.objects.get(id=id)
    form=JumlahForm(instance=data)
    return render(request,"jumlah/edit.html",{"form":form,"id":id})

@login_required
def update(request,id):
    if request.POST:
        form = JumlahForm(request.POST)
        if form.is_valid():
          data=Jumlah.objects.get(pk=id)
          form=JumlahForm(request.POST,instance=data)
          form.save()
          return HttpResponse("ok")
        else:
            data=Jumlah.objects.get(pk=id)
            form=JumlahForm(instance=data)
            return HttpResponse("no oke")

@login_required
def delete(request,data):
    id=decript(data)
    item = Jumlah.objects.get(id=id)
    item.delete()
    return redirect("/jumlah", messages.success(request, 'Item Was successfully deleted', 'alert-success'))