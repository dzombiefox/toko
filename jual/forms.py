from django import forms
from .models import Jual

class JualForm(forms.ModelForm):
    class Meta :
        model =Jual
        fields=["tanggal","namaPembeli","statusPembeli","pembayaran","potongan","keterangan","posted_by","bayar"]