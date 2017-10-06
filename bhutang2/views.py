# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Bhutang
from forms import BhutangForm
from biaya .models import Biaya
from bmasuk .models import Bmasuk

# Create your views here.

def index(request,id):
    bmasuk=Bmasuk.objects.filter(masuk=id)
    biaya=Biaya.objects.filter(masuk=id)
    form=BhutangForm()
    return render(request,"bhutang/index.html",{"bmasuk":bmasuk,"biaya":biaya,"form":form,"masuk":id})

def save(request):
        form=BhutangForm(request.POST)
        form.save()
        return HttpResponse("bagudung")
     #   return redirect(request.META['HTTP_REFERER'])


