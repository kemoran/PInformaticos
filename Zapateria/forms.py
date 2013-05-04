from django import forms
from Zapateria.models import *

class FrmContrasena(forms.Form):
    Nueva_Contrasena = forms.CharField(widget=forms.PasswordInput)
    
class FrmZapateria(forms.ModelForm): # Formulario para Agregar y Editar Empresas.
    class Meta:
        model = TblZapateria
        exclude = ('id_zapateria')
