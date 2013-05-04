from django import forms
from Zapateria.models import *

class FrmContrasena(forms.Form):
    Nueva_Contrasena = forms.CharField(widget=forms.PasswordInput)
    
class FrmZapateria(forms.ModelForm): # Formulario para Agregar y Editar Empresas.
    class Meta:
        model = TblZapateria
        exclude = ('id_zapateria')

class FrmTalla(forms.ModelForm):
    class Meta:
        model = TblTalla
        exclude = ('id_talla')
        
class FrmColor(forms.ModelForm):
    class Meta:
        model = TblColor
        exclude = ('id_color')

class FrmTipo(forms.ModelForm):
    class Meta:
        model = TblTipo
        exclude = ('id_tipo')

class FrmEstilo(forms.ModelForm):
    class Meta:
        model = TblEstilo
        exclude = ('id_estilo')

class FrmMarca(forms.ModelForm):
    class Meta:
        model = TblMarca
        exclude = ('id_marca')
        
