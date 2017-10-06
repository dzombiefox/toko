from django import forms
from .models import EkstrakStok

# from .models import


class FormEkstrakStok(forms.ModelForm):
    class Meta :
        model = EkstrakStok
        fields = ["stok","jumlahawal","satuan","jumlahekstrak","keterangan","posted_by"]