# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Suplier
from forms import SuplierForm
from functions .functions import decript
# Create your views here.

@login_required
def index(request):
    data=Suplier.objects.all()
    return render(request,"suplier/index.html",{"suplier":data})

@login_required
def add(request):
    form = SuplierForm()
    return render(request,"suplier/add.html",{"form":form})

@login_required
def save(request):
    form = SuplierForm(request.POST)
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
    data=Suplier.objects.get(id=decript(data))
    form=SuplierForm(instance=data)
    return render(request,"suplier/edit.html",{"form":form,"id":id})

@login_required
def update(request,id):
    if request.POST:
        form = SuplierForm(request.POST)
        if form.is_valid():
          data=Suplier.objects.get(pk=id)
          form=SuplierForm(request.POST,instance=data)
          form.save()
          return HttpResponse("ok")
        else:
            data=Suplier.objects.get(pk=id)
            form=SuplierForm(instance=data)
            return HttpResponse("no oke")

@login_required
def delete(request,data):
    item = Suplier.objects.get(id=decript(data))
    item.delete()
    return redirect("/suplier", messages.success(request, 'Item Was successfully deleted', 'alert-success'))