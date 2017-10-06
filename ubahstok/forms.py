from django import forms
from .models import UbahStok

class UbahStokForm(forms.ModelForm):
   class Meta :
       model = UbahStok
       fields =["stok","jumlah","stokawal","posted_by","keterangan"]

