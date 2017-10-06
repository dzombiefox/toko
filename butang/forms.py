from django import forms
from .models import Butang

class ButangForm(forms.ModelForm):
    class Meta :
        model =Butang
        fields=["tanggal","penerima","jumlahHutang","jumlahBayar","masuk","posted_by"]
