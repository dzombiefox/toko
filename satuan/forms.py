from django import forms
from .models import Satuan

class SatuanForm(forms.ModelForm):
    class Meta :
        model =Satuan
        fields=["namaSatuan","posted_by"]