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
        
class FrmProveedor(forms.ModelForm):
    class Meta:
        model = TblProveedor
        exclude = ('id_proveedor')
        
class FrmTipoEntrada(forms.ModelForm):
    class Meta:
        model = TblTipoEntrada
        exclude = ('id_tipo_entrada')
        
class FrmTipoSalida(forms.ModelForm):
    class Meta:
        model = TblTipoSalida
        exclude = ('id_tipo_salida')

class FrmCobrador(forms.ModelForm):
    genero_personal = forms.ChoiceField(choices=GENERO, widget=forms.RadioSelect())
    fecha_nacimiento_personal = forms.CharField(widget=forms.TextInput(attrs={'data-date-format':'yyyy-mm-dd' , 'class':'datepicker'}))
    Nombre_de_usuario = forms.CharField()
    Contrasena = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = TblPersonal
        fields = ('nombre_personal',
                  'apellido_personal',
                  'genero_personal',
                  'fecha_nacimiento_personal',
                  'dui_personal',
                  'nit_personal',
                  'telefono_personal',
                  'direccion_personal',
                  'correo_electronico_personal')

class FrmCobradorEditar(forms.ModelForm):
    class Meta:
        model = TblPersonal
        fields = ('telefono_personal',
                  'direccion_personal',
                  'correo_electronico_personal')
        