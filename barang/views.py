# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Barang
from forms import BarangForm
from functions .functions import decript
# Create your views here.
from django.core import serializers

@login_required
def index(request):
    data=Barang.objects.all()
    return render(request,"barang/index.html",{"barang":data})

@login_required
def add(request):
    form=BarangForm()
    return render(request,"barang/add.html",{"form":form})

@login_required
def save(request):
    form = BarangForm(request.POST)
    if form.is_valid():
        if form.save():
            return HttpResponse("Berhasil Menambah Data")
        else:
            return HttpResponse("No oke")
    else:
        return HttpResponse("form failed")

@login_required
def edit(request,data):
    id=decript(data)
    data=Barang.objects.get(id=decript(data))
    form=BarangForm(instance=data)
    #return HttpResponse(form)
    return render(request,"barang/edit.html",{"form":form,"id":id})

@login_required
def update(request,id):
    if request.POST:
        form = BarangForm(request.POST)
        if form.is_valid():
          data=Barang.objects.get(pk=id)
          form=BarangForm(request.POST,instance=data)
          form.save()
          return HttpResponse("ok")
        else:
            data=Barang.objects.get(pk=id)
            form=BarangForm(instance=data)
            return HttpResponse("no oke")


@login_required
def delete(request,data):
    item = Barang.objects.get(id=decript(data))
    item.delete()
    return redirect("/barang", messages.success(request, 'Item Was successfully deleted', 'alert-success'))