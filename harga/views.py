# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from models import Harga
from forms import HargaForm
from functions .functions import decript
# Create your views here.

@login_required
def index(request):
    data=Harga.objects.all()
    return render(request,"harga/index.html",{"harga":data})

@login_required
def add(request):
    form=HargaForm()
    return render(request, "harga/add.html", {"form": form})

@login_required
def save(request):
    form = HargaForm(request.POST)
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
    data=Harga.objects.get(id=id)
    form=HargaForm(instance=data)
    return render(request,"harga/edit.html",{"form":form,"id":id})

@login_required
def update(request,id):
    if request.POST:
        form = HargaForm(request.POST)
        if form.is_valid():
          data=Harga.objects.get(pk=id)
          form=HargaForm(request.POST,instance=data)
          form.save()
          return HttpResponse("ok")
        else:
            data=Harga.objects.get(pk=id)
            form=HargaForm(instance=data)
            return HttpResponse("no oke")

@login_required
def delete(request,data):
    id=decript(data)
    item = Harga.objects.get(id=id)
    item.delete()
    return redirect("/harga", messages.success(request, 'Item Was successfully deleted', 'alert-success'))