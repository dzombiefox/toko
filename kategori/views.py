# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from models import Kategori
from forms import KategoriForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from functions .functions import decript
# Create your views here.

@login_required
def index(request):
    kategori=Kategori.objects.all()
    return render(request, "kategori/index.html",{"data":kategori})

@login_required
def add(request):
    form = KategoriForm()
    return render(request,"kategori/add.html",{"form":form})

@login_required
def save(request):
    form = KategoriForm(request.POST)
    if form.is_valid():
        if form.save():
          return HttpResponse("Berhasil Menambah Data")
        else:
          return  HttpResponse("No oke")
    else:
        return HttpResponse("form failed")

@login_required
def edit(request,data):
    id=decript(data)
    data=Kategori.objects.get(id=decript(data))
    form=KategoriForm(instance=data)
    return render(request,"kategori/edit.html",{"form":form,"id":id})

@login_required
def update(request,id):
    if request.POST:
        form = KategoriForm(request.POST)
        if form.is_valid():
          data=Kategori.objects.get(pk=id)
          form=KategoriForm(request.POST,instance=data)
          form.save()
          return HttpResponse("ok")
        else:
            data=Kategori.objects.get(pk=id)
            form=KategoriForm(instance=data)
            return HttpResponse("no oke")

@login_required
def delete(request,data):
    item = Kategori.objects.get(id=decript(data))
    item.delete()
    return redirect("/kategori", messages.success(request, 'Item Was successfully deleted', 'alert-success'))