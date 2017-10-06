# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from models import Bmasuk
from stok .models import Stok
from forms import BarangMasukForm
from serializers import BmasukSerializer
from rest_framework import generics
# Create your views here.
@login_required
def save(request):
    form = BarangMasukForm(request.POST)

    if form.is_valid():
        data = form.cleaned_data
        barang = data['barang']
        satuan = data['satuan']
        jumlah = data['jumlah']
        harga = data['harga']
        masuk = data['masuk']

        cekBarang = Bmasuk.objects.filter(barang=barang, satuan=satuan, masuk=masuk)
        if cekBarang.exists():
            bmasuk = Bmasuk.objects.get(barang=barang, satuan=satuan, masuk=masuk)
            jumlahBarang = bmasuk.jumlah
            totalJumlah = jumlahBarang + jumlah
            Bmasuk.objects.filter(pk=bmasuk.id).update(jumlah=totalJumlah, harga=harga)

        else:
            form.save()
        cek = Stok.objects.filter(barang=barang, satuan=satuan)
        if cek.exists():
            stok = Stok.objects.get(barang=barang, satuan_id=satuan)
            Stok.objects.filter(pk=stok.id).update(barang=barang, satuan=satuan, stok=stok.stok + jumlah)
            return HttpResponse("ok")
        else:
            datastok = Stok(barang=barang, satuan=satuan, stok=jumlah)
            datastok.save()
            return HttpResponse("no ok")


# def getBarang(request,id):
#     data = Bmasuk.objects.all()
#     return HttpResponse(serializers.serialize('json', data))

# class GetBarang(request):
#     return HttpResponse(json(Bmasuk.objects.filter(id=1)))
    # data=Bmasuk.objects.all(is_active=True)
    # serializer_bmasuk=BmasukSerializer(data,many=True)
    # return Response(serializer_bmasuk.data)

class GetBarangJson(generics.ListAPIView):
    serializer_class = BmasukSerializer
    def get_queryset(self):
        id=self.kwargs['id']
        return Bmasuk.objects.filter(masuk=id)


    # def get_object(self,pk):
    #     try :
    #         return Bmasuk.objects.get(pk=pk)
    #     except Bmasuk.DoesNotExist:
    #         raise Http404
    # def get(self,request,pk,format=None):
    #     data=self.get_object(pk)
    #     serializer_bmasuk=BmasukSerializer(data)
    #     return Response(serializer_bmasuk)
    # queryset = Bmasuk.objects.get(pk=2)
    # serializer_class = BmasukSerializer

        # return HttpResponse("ok")

        # def get_object(self,pk):
        #     try:
        #         return Bmasuk.objects.get(pk=pk)
        #     except Bmasuk.DoesNotExist:
        #         raise Http404
        # def get(self,request,pk,format=None):
        #     bmasuk=self.get_object(pk=pk)


    # queryset = Bmasuk.objects.all()
    # serializer_class = BmasukSerializer
@login_required
def delete(request,id):
        item = Bmasuk.objects.get(id=id)
        satuan=item.satuan
        barang=item.barang
        jumlah=item.jumlah
        stok=Stok.objects.get(satuan=satuan,barang=barang)
        jumlahstok=stok.stok
        Stok.objects.filter(pk=stok.id).update(barang=barang, satuan=satuan, stok=stok.stok - jumlah)
        # return HttpResponse(stok.stok)
        item.delete()
        return HttpResponse("ok")
        #item.delete()



