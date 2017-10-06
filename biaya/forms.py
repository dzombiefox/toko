from django import forms
from .models import Biaya

class BiayaForm(forms.ModelForm):
    class Meta :
        model =Biaya
        fields=["namaBiaya","masuk","jumlahBiaya"]