from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Butang
from forms import ButangForm
from biaya .models import Biaya
from bmasuk .models import Bmasuk
from rmasuk .models import Rmasuk
from masuk .models import Masuk
from functions .functions import decript
# Create your views here.
@login_required
def index(request,data):
    id = decript(data)
    form = ButangForm()
    bmasuk=Bmasuk.objects.filter(masuk=id)
    biaya=Biaya.objects.filter(masuk=id)
    butang=Butang.objects.filter(masuk=id)
    dmasuk=Masuk.objects.get(pk=id)
    totalHutang=0
    sumButang=0
    totalBmasuk =0
    totalRmasuk = 0
    for dbmasuk in butang :
        sumButang += dbmasuk.jumlahBayar

    for dbmasuk in bmasuk:
        totalBmasuk +=  int(dbmasuk.jumlah) * int(dbmasuk.harga)
        bmasuk = dbmasuk.id
        rmasuk = Rmasuk.objects.filter(bmasuk=bmasuk)
        for drmasuk in rmasuk :
            totalRmasuk += int(drmasuk.jumlahRetur) * int(dbmasuk.harga)

    totalHutang = int(totalBmasuk) - int (totalRmasuk) - int (sumButang)

    return render(request,"bhutang/index.html",{"bmasuk":bmasuk,"biaya":biaya,"form":form,"masuk":id,"sumbutang":totalHutang,"butang":butang,"dmasuk":dmasuk})

@login_required
def save(request):
        form=ButangForm(request.POST)
        jumlahHutang=request.POST['jumlahHutang']
        jumlahBayar=request.POST['jumlahBayar']
        sisaHutang = int (jumlahHutang) - int (jumlahBayar)
        masuk=request.POST['masuk']
        if sisaHutang < 0 :
            return redirect(request.META['HTTP_REFERER'],messages.add_message(request, messages.INFO, 'Maaf jumlah bayar tidak boleh melebihi hutang'))
        elif sisaHutang == 0:
            form.save()
            bmasuk=Bmasuk.objects.filter(masuk=masuk)
            for data in bmasuk :
                rmasuk=Rmasuk.objects.filter(bmasuk=data.id)
                for item in rmasuk :
                    Rmasuk.objects.filter(bmasuk=data.id).update(rmasukStatus=1)
            Masuk.objects.filter(pk=masuk).update(status=1)

        elif sisaHutang > 0 :
            form.save()
            return redirect(request.META['HTTP_REFERER'])
        # return HttpResponse("ok")
        return redirect(request.META['HTTP_REFERER'])

@login_required
def data(request):
    data=Butang.objects.all()
    return render(request,"bhutang/data,")

@login_required
def delete(request,id):
    item = Butang.objects.get(id=id)
    Masuk.objects.filter(pk=item.masuk_id).update(status=0)
    item.delete()
    return redirect(request.META['HTTP_REFERER'])

@login_required
def prints(request,id):
    return render(request,"bhutang/print.html")