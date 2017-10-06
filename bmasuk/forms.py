from django import forms
from .models import Bmasuk

class BarangMasukForm(forms.ModelForm):
    class Meta :
        model =Bmasuk
        fields=["masuk","barang","satuan","jumlah","harga","posted_by"]
        widgets = {
            'summary': forms.Select(attrs={'width:100%'}),
        }