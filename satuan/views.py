# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Satuan
from forms import SatuanForm
from functions .functions import decript
# Create your views here.

@login_required
def index(request):
    data=Satuan.objects.all()
    return render(request,"satuan/index.html",{"satuan":data})

@login_required
def add(request):
    form=SatuanForm()
    return render(request, "satuan/add.html", {"form": form})

@login_required
def save(request):
    form = SatuanForm(request.POST)
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
    data=Satuan.objects.get(id=decript(data))
    form=SatuanForm(instance=data)
    return render(request,"satuan/edit.html",{"form":form,"id":id})

@login_required
def update(request,id):
    if request.POST:
        form = SatuanForm(request.POST)
        if form.is_valid():
          data=Satuan.objects.get(pk=id)
          form=SatuanForm(request.POST,instance=data)
          form.save()
          return HttpResponse("ok")
        else:
            data=Satuan.objects.get(pk=id)
            form=SatuanForm(instance=data)
            return HttpResponse("no oke")

@login_required
def delete(request,data):
    item = Satuan.objects.get(id=decript(data))
    item.delete()
    return redirect("/satuan", messages.success(request, 'Item Was successfully deleted', 'alert-success'))