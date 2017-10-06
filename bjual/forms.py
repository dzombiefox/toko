from django import forms
from .models import Bjual

class BarangJualForm(forms.ModelForm):
    class Meta :
        model =Bjual
        fields=["barang","satuan","jual","hargaModal","hargaJual","jumlahJual","hargalain","pilihan"]

