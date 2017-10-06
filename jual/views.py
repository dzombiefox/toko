from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import JualForm
from bjual .forms import BarangJualForm
from rjual .forms import RjualForm
from .models import Jual
from django.contrib.auth.models import User
from bjual .models import Bjual
from django.db.models import Q
from functions .functions import decript
from rjual .models import Rjual
from stok .models import Stok
from ekstrakstok .forms import FormEkstrakStok
from harga .models import  Harga
@login_required
def index(request):
    jual=Jual.objects.all()
    return render(request,"jual/index.html",{"jual":jual})

@login_required
def add(request):
    form=JualForm()
    frm=BarangJualForm()
    return render(request,"jual/add.html",{"form":form,"frm":frm})

@login_required
def save(request):
    # return HttpResponse("boko")
    form = JualForm(request.POST)
    if form.is_valid():
        c = form.save(commit=False)
        c.save()
        cekdetail = Jual.objects.filter(~Q(id=c.id), bjual__isnull=True)
        cekdetail.delete()
        return HttpResponse(c.id)

@login_required
def edit(request,data) :
    # return HttpResponse("OK")
    id = decript(data)
    data = Jual.objects.get(pk=id)
    form =JualForm(instance=data)
    frm = BarangJualForm()
    frjual =RjualForm()
    rjual = Rjual.objects.filter(bjual__jual=id)
    # return render(request,"tes/index.html",{"data":rjual})
    return render(request,"jual/edit.html",{"form":form,"frm":frm,"data":data,"frjual":frjual,"rjual":rjual})

@login_required
def update(request):
    id=request.POST["jual"]
    tanggal=request.POST["tanggal"]
    pembeli = request.POST["namaPembeli"]
    pembayaran = request.POST["pembayaran"]
    statusPembeli = request.POST["statusPembeli"]
    potongan = request.POST["potongan"]
    bayar = request.POST["bayar"]
    keterangan = request.POST["keterangan"]
    Jual.objects.filter(pk=id).update(tanggal=tanggal, namaPembeli=pembeli, pembayaran=pembayaran,statusPembeli=statusPembeli,potongan=potongan,keterangan=keterangan,bayar=bayar)

    return HttpResponse("oke coy")

@login_required
def prints(request,id):
    jual=Jual.objects.get(pk=id)
    bayar=jual.bayar
    bjual=Bjual.objects.filter(jual=id).order_by('pilihan')
    barangJual=Bjual.objects.filter(jual=id,pilihan=0)
    total = 0
    for data in barangJual:
        total +=int (data.hargaJual) * int (data.jumlahJual)

    totalBayar =int(total) - int(jual.potongan)
    sisabayar=int(totalBayar)-int(bayar)
    sisaKembali = int(jual.bayar)-int(total)
    sisa = 0
    kembali = 0
    if sisaKembali > 0 :
        kembali =sisaKembali
    else:
        kembali = 0

    if(sisabayar == 0 ):
        sisa = 0
    elif sisabayar < 0:
        sisa = 0
    else:
        sisa = sisabayar

    return render(request,"jual/print.html",{"jual":jual,"bjual":bjual,"total":total,"totalBayar":totalBayar,"sisa":sisa,"kembali":kembali})

@login_required
def report(request):
    if request.POST:
        date1 = request.POST['date1']
        date2 = request.POST['date2']
        data = Bjual.objects.filter(jual__tanggal__range=(date1,date2))
        jual =Jual.objects.filter(tanggal__range=(date1,date2))
        return render(request,"jual/report.html",{"datas":data,"jual":jual,"date1":date1,"date2":date2})
    else :
        return render(request, "jual/report.html",{"date1":"2001-12-12","date2":"2001-12-12"})

def modalstok(request,id):
    fr = FormEkstrakStok()
    stok =Stok.objects.filter(barang_id=id)
    return render(request,"jual/modalstok.html",{"data":stok,"frm":fr,"id":id})

def getprice(request,barang,satuan):
    harga = Harga.objects.filter(barang_id=barang, satuan_id=satuan)
    if harga.exists():
         harga=Harga.objects.get(barang_id=barang,satuan_id=satuan)
         return HttpResponse(harga.jual)
    else :
        return HttpResponse("0")