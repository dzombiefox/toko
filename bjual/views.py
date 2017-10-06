from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from models import Bjual
from stok .models import Stok
from .forms import BarangJualForm
from harga .models import Harga
from django.contrib.auth.models import User
from barang .models import Barang
from satuan .models import Satuan
from jual .models import Jual
from serializers import BjualSerializer
from rest_framework import generics
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from rest_framework.response import Response
from django.http import JsonResponse
from django.db.models import Q
from jumlah .models import Jumlah
@login_required
def save(request):
    # return HttpResponse("kok")
    form=BarangJualForm(request.POST)

    barang=request.POST["barang"]

    satuan =request.POST["satuan"]
    jual =request.POST["jual"]
    jumlah =request.POST["jumlahJual"]
    pilihan=request.POST['pilihan']

    cekHarga=Harga.objects.filter(barang=barang,satuan=satuan)

    # harga = Harga.objects.get(barang=barang, satuan=satuan)
    # return HttpResponse(harga.barang)

    if cekHarga.exists():

        harga=Harga.objects.get(barang=barang,satuan=satuan)
        cekStok=Stok.objects.filter(barang=barang,satuan=satuan)
     #   getstok = Stok.objects.get(barang=barang, satuan=satuan)

        if cekStok.exists():
            getstok=Stok.objects.get(barang=barang,satuan=satuan)
            stok=getstok.stok
            if stok == 0 :
                return HttpResponse("2")
            else :
                jml=int(stok) - int(jumlah)
                if jml < 0 :
                    return HttpResponse("3")
                else :
                    Stok.objects.filter(pk=getstok.id).update(stok=jml)
                    modal = harga.modal
                    hargajual = 0
                    hargalain = request.POST['hargalain']
                    # return HttpResponse(hargalain)
                    if hargalain == "" or hargalain == "0" :
                        hargajual  = harga.jual
                    else :
                        hargajual = hargalain
                    if pilihan == "0" :
                        cekBarang = Bjual.objects.filter(barang=barang, satuan=satuan, jual_id=jual, pilihan=0)
                        if cekBarang.exists():
                            bjual = Bjual.objects.get(barang=barang, satuan=satuan, jual_id=jual, pilihan=0)
                            jumlahBarang = bjual.jumlahJual
                            totalJumlah = int(jumlahBarang) + int(jumlah)
                            Bjual.objects.filter(pk=bjual.id).update(jumlahJual=totalJumlah)
                            return HttpResponse("update")
                        else:
                            bmasuk = Bjual(hargaModal=modal, hargaJual=hargajual, jumlahJual=jumlah, pilihan=pilihan,
                                           barang_id=barang, satuan_id=satuan, jual_id=jual)
                            bmasuk.save()
                            return HttpResponse("odk")
                    else :
                        cekBarang = Bjual.objects.filter(barang=barang, satuan=satuan, jual_id=jual, pilihan=1)
                        if cekBarang.exists():
                            bjual = Bjual.objects.get(barang=barang, satuan=satuan, jual_id=jual, pilihan=1)
                            jumlahBarang = bjual.jumlahJual
                            totalJumlah = int(jumlahBarang) + int(jumlah)
                            Bjual.objects.filter(pk=bjual.id).update(jumlahJual=totalJumlah)
                            return HttpResponse("update")
                        else:
                            bmasuk = Bjual(hargaModal=modal, hargaJual=hargajual, jumlahJual=jumlah, pilihan=pilihan,
                                           barang_id=barang, satuan_id=satuan, jual_id=jual)
                            bmasuk.save()
                            return HttpResponse("odk")


        else:
            return HttpResponse("1")
    else :
        return HttpResponse("0")


    return HttpResponse(barang)

@login_required
def delete(request,id):
    cekBarang=Bjual.objects.get(pk=id)
    barang = cekBarang.barang
    satuan = cekBarang.satuan
    jumlahJual = cekBarang.jumlahJual
    jualid = cekBarang.jual
    getstok = Stok.objects.get(satuan=satuan,barang=barang)
    stok=getstok.stok
    updatestok = int(stok) + int(jumlahJual)
    Stok.objects.filter(pk=getstok.id).update(stok=updatestok)
    item = Bjual.objects.get(id=id)
    item.delete()
    return HttpResponse("ok")


class GetJualJson(generics.ListAPIView):
    serializer_class = BjualSerializer
    def get_queryset(self):
        id=self.kwargs['id']
        return Bjual.objects.filter(jual=id).order_by('pilihan')


def tes(request):
    # return HttpResponse('sd')
    stok = Stok.objects.filter(barang_id=8,satuan_id=11)
    if stok.exists():
        return HttpResponse("yes")
    else :
        # return HttpResponse("ble e")
        jumlah = Jumlah.objects.get(barang_id=8,satuanKecil_id =11)
        # cekstok = Stok.objects.filter(barang_id=8)
        # return HttpResponse(jumlah.jumlah)
        # for st in cekstok :
        #    return HttpResponse(st.barang)
        # for item in jumlah:
        #     return HttpResponse(item.id)

        # cek = Jumlah.objects.get(barang_id=8,satuanKecil_id=11)
        # return HttpResponse(cek.id)

    # return HttpResponse("bengeak")
    # cekdetail =Jual.objects.filter(~Q(id=171))
    # cekdetail=Jual.objects.filter(~Q(id=175),bjual__isnull=True)
    # cekdetail.delete()
    # return render(request,"tes/index.html",{"data":cekdetail})
    return HttpResponse(stok.id)
# def tes(self,request,**kwargs):
#     try :
#         data =Bjual.objects.all()
#         serializer =BjualSerializer(data,many=True)
#         return Response(serializer.data,content_type=None)
#     except Exception as e :
#         return Response(e.message)

