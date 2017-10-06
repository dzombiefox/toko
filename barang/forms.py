from django import forms
from .models import Barang

class BarangForm(forms.ModelForm):
    class Meta :
        model =Barang
        fields=["kodeBarang","namaBarang","kategory","posted_by"]