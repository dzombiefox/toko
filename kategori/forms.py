from django import forms
from .models import Kategori

class KategoriForm(forms.ModelForm):
    class Meta :
        model =Kategori
        fields=["namaKategori","posted_by"]