# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from models import Biaya
from stok .models import Stok
from forms import BiayaForm
from serializers import BiayaSerializer
from rest_framework import generics

# Create your views here.

def save(request):
    form = BiayaForm(request.POST)
    if form.is_valid():
       form.save()
       return HttpResponse("okok")
    else:
        HttpResponse("no oke")
       #data = form.cleaned_data


class GetBiayaJson(generics.ListAPIView):
    serializer_class = BiayaSerializer
    def get_queryset(self):
        id=self.kwargs['id']
        return Biaya.objects.filter(masuk=id)

def delete(request,id):
      item = Biaya.objects.get(id=id)
      item.delete()
      return HttpResponse("ok")

