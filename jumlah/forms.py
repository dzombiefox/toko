from django import forms
from .models import Jumlah

class JumlahForm(forms.ModelForm):
    class Meta :
        model =Jumlah
        fields=["barang","satuanBesar","satuanKecil","jumlah","posted_by"]