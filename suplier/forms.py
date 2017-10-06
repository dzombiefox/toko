from django import forms
from .models import Suplier

class SuplierForm(forms.ModelForm):
    class Meta :
        model =Suplier
        fields=["namaSuplier","namaToko","alamatToko","status","posted_by"]