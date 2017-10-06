from django import forms
from .models import Masuk

class MasukForm(forms.ModelForm):
    class Meta :
        model =Masuk
        fields=["id","tanggal","nota","suplier","sales","pembayaran","jangkaWaktu","keterangan","status","posted_by"]