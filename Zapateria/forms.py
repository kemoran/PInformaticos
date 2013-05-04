from django import forms
from Zapateria.models import *

class FrmContrasena(forms.Form):
    Nueva_Contrasena = forms.CharField(widget=forms.PasswordInput)