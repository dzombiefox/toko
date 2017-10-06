from django import forms
from .models import Stok

class StokForm(forms.ModelForm):
    class Meta :
        model =Stok
        fields=["barang","satuan","stok"]