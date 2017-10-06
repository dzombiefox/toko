# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Masuk
from forms import MasukForm
from rmasuk .forms import RmasukForm
from bmasuk .forms import BarangMasukForm
from biaya .forms import BiayaForm
from bmasuk .models import Bmasuk
from biaya .models import Biaya
from rmasuk .models import Rmasuk
from django.db.models import Q
from functions .functions import decript
# Create your views here.

@login_required
def index(request):
    data=Masuk.objects.all()
    return render(request,"masuk/index.html",{"masuk":data})

@login_required
def add(request):
    fbarang=BarangMasukForm()
    fbiaya=BiayaForm()
    form=MasukForm()
    return render(request, "masuk/add.html", {"form": form,"frm":fbarang,"fbi":fbiaya})

@login_required
def edit(request,data):
    id = decript(data)

    data = Masuk.objects.get(id=id)
    form = MasukForm(instance=data)
    fbarang = BarangMasukForm()
    fbiaya = BiayaForm()
    frmasuk=RmasukForm()
    bmasuk=Bmasuk.objects.filter(masuk_id=id)
    biaya=Biaya.objects.filter(masuk_id=id)
    rmasuk=Rmasuk.objects.filter(bmasuk__masuk=id)
    masuk=Masuk.objects.get(pk=id)
    # return render(request,"masuk/tes.html",{"rmasuk":rmasuk})
    return render(request, "masuk/edit.html", {"form": form,"frm":fbarang,"fbi":fbiaya,"id":id,"bmasuk":bmasuk,"biaya":biaya,"frma":frmasuk,"rmasuk":rmasuk,"masuk":masuk})

@login_required
def save(request):
    form = MasukForm(request.POST)

    if form.is_valid():
        c = form.save(commit=False)
        status=form.cleaned_data['pembayaran']
        c.status=status
        c.save()
        cekdetail = Masuk.objects.filter(~Q(id=c.id), bmasuk__isnull=True)
        cekdetail.delete()
        return HttpResponse(c.id)
    else:
        return HttpResponse("form failed")

@login_required
def update(request,id):
    if request.POST:
        form = MasukForm(request.POST)
        if form.is_valid():
            data = Masuk.objects.get(pk=id)
            form = MasukForm(request.POST, instance=data)
            form.save()
            return HttpResponse("ok")
        else:
            data = Masuk.objects.get(pk=id)
            form = MasukForm(instance=data)
            return HttpResponse("no oke")

