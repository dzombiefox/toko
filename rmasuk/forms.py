from django import forms
from .models import Rmasuk

class RmasukForm(forms.ModelForm):
    class Meta :
        model =Rmasuk
        fields=["bmasuk","jumlahRetur","keterangan","rmasukStatus","posted_by"]