from django import forms
from .models import Harga

class HargaForm(forms.ModelForm):
    class Meta :
        model =Harga
        fields=["barang","satuan","modal","jual","posted_by"]