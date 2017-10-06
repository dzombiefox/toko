from django import forms
from .models import Bhutang

class BhutangForm(forms.ModelForm):
    class Meta :
        model =Bhutang
        fields=["tanggal","penerima","jumlahHutang","jumlahBayar","sisaHutang","masuk","posted_by"]