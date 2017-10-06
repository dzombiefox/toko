from django import forms
from .models import Rjual

class RjualForm(forms.ModelForm):
    class Meta :
        model =Rjual
        fields=["bjual","jumlah","pilihan","keterangan","posted_by"]