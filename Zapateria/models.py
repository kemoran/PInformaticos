from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationErro
import re

# Create your models here.

GENERO = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

def ValidarDUI(value):
    if re.match("^\d{8}-\d{1}$", value == None:
        raise ValidationError(u'%s DUI Incorrecto' % value)

def ValidarLetra(value):
    if re.match("^\W+$", value) == None:
        raise ValidationError(u'%s Dato Incorrecto' % value)

def ValidarNumero(value):
    if re.match("^\d+$", value) == None:
        raise ValidationError(u'%s Dato Incorrecto' % value)

def ValidarNIT(value):
    if re.match("^\d{4}-\d{6}-\d{3}-\d{1}$", value) == None:
        raise ValidationError(u'%s NIT Incorrecto' % value)

def ValidarTelefono(value):
    if re.match("^\d{4}-\d{4}$", value) == None:
        raise ValidationError(u'%s Numero de Telefono Incorrecto' % value)

def ValidarCorreo(value):
    if re.match("^\w+@\w+\.\S+$", value) == None:
        raise ValidationError(u'%s Correo Incorrecto' % value)


class TblZapateria(models.Model):
    id_zapateria = models.AutoField(primary_key=True)
    nombre_zapateria = models.CharField(max_length=50, help_text="Ejemplo: Calzado Ideal")
    numero_registro_zapateria = models.CharField(max_length=7, help_text="Ejemplo: 0000-0")
    nit_zapateria = models.CharField(max_length=17, help_text="Ejemplo: 0000-000000-000-0", validators=[ValidarNIT])
    direccion_zapateria = models.CharField(max_length=75, help_text="Ejemplo: Calle 15 de septiembre, Bo San Pedro 12, Metapan, Santa Ana")
    telefono_zapateria = models.CharField(max_length=9, blank=True, help_text="Ejemplo: 0000-0000", validators=[ValidarTelefono])
    correo_electronico_zapateria = models.CharField(max_length=50, blank=True, help_text="Ejemplo: ejemplo@ejemplo.com", validators=[ValidarCorreo])
    pagina_web_zapateria = models.CharField(max_length=50, blank=True, help_text="Ejemplo: www.calzadoideal.com")
    class Meta:
        db_table = u'tbl_zapateria'

class TblTipoEntrada(models.Model):
    id_tipo_entrada = models.AutoField(primary_key=True)
    descripcion_tipo_entrada = models.CharField(max_length=50, help_text="Ejemplo: Compra", validators=[ValidarLetra])
    class Meta:
        db_table = u'tbl_tipo_entrada'

class TblTipoSalida(models.Model):
    id_tipo_salida = models.AutoField(primary_key=True)
    descripcion_tipo_salida = models.CharField(max_length=50, help_text="Ejemplo: Venta", validators=[ValidarLetra])
    class Meta:
        db_table = u'tbl_tipo_salida'

class TblEntrada(models.Model):
    id_entrada = models.AutoField(primary_key=True)
    id_tipo_entrada = models.ForeignKey(TblTipoEntrada, db_column='id_tipo_entrada')
    user = models.ForeignKey(User, unique=True)
    numero_factura = models.CharField(max_length=7, help_text="Ejemplo: 0000000", validators=[ValidarNumero])
    fecha_entrada = models.DateField()
    estado_entrada = models.CharField(max_length=1)
    comentario_entrada = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = u'tbl_entrada'

class TblEstilo(models.Model):
    id_estilo = models.AutoField(primary_key=True)
    descripcion_estilo = models.CharField(max_length=30, help_text="Ejemplo: Casual", validators=[ValidarLetra])
    class Meta:
        db_table = u'tbl_estilo'

class TblMarca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    descripcion_marca = models.CharField(max_length=30, help_text="Ejemplo: ADOC5000")
    class Meta:
        db_table = u'tbl_marca'

class TblPersonal(models.Model):
    id_personal = models.AutoField(primary_key=True)
    id_zapateria = models.ForeignKey(TblZapateria, db_column='id_zapateria')
    user = models.ForeignKey(User, unique=True)
    nombre_personal = models.CharField(max_length=30, help_text="Ejemplo: Juan", validators=[ValidarLetra])
    apellido_personal = models.CharField(max_length=30, help_text="Ejemplo: Perez", validators=[ValidarLetra])
    genero_personal = models.CharField(max_length=1, choices=GENERO)
    fecha_nacimiento_personal = models.DateField()
    dui_personal = models.CharField(max_length=10, help_text="Ejemplo: 00000000-0", validators=[ValidarDUI])
    nit_personal = models.CharField(max_length=17, help_text="Ejemplo: 0000-000000-000-0", validators=[ValidarNIT])
    telefono_personal = models.CharField(max_length=9, help_text="Ejemplo: 0000-0000", validators=[ValidarTelefono])
    direccion_personal = models.CharField(max_length=100, blank=True, help_text="Ejemplo: Direccion de Empleado")
    correo_electronico_personal = models.CharField(max_length=50, blank=True, help_text="Ejemplo: ejemplo@ejemplo.com", validators=[ValidarCorreo])
    class Meta:
        db_table = u'tbl_personal'

class TblProveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=30, help_text="Ejemplo: ADOC")
    direccion_proveedor = models.CharField(max_length=75, blank=True, help_text="Ejemplo: Direccion del ")
    telefono_proveedor = models.CharField(max_length=9, help_text="Ejemplo: 0000-0000", validators=[ValidarTelefono])
    fax_proveedor = models.CharField(max_length=9, blank=True, help_text="Ejemplo: 0000-0000", validators=[ValidarTelefono])
    correo_electronico_proveedor = models.CharField(max_length=50, blank=True, help_text="Ejemplo: ejemplo@ejemplo.com", validators=[ValidarCorreo])
    class Meta:
        db_table = u'tbl_proveedor'

class TblSalida(models.Model):
    id_salida = models.AutoField(primary_key=True)
    id_tipo_salida = models.ForeignKey(TblTipoSalida, db_column='id_tipo_salida')
    user = models.ForeignKey(User, unique=True)
    numero_factura = models.CharField(max_length=7, help_text="Ejemplo: 0000000", validators=[ValidarNumero])
    fecha_salida = models.DateField()
    estado_salida = models.CharField(max_length=1)
    comentario_salida = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = u'tbl_salida'

class TblColor(models.Model):
    id_color = models.AutoField(primary_key=True)
    descripcion_color = models.CharField(max_length=20, help_text="Ejemplo: Blanco", validators=[ValidarLetra])
    class Meta:
        db_table = u'tbl_color'

class TblTalla(models.Model):
    id_talla = models.AutoField(primary_key=True)
    descripcion_talla = models.CharField(max_length=2, help_text="Ejemplo: 00", validators=[ValidarNumero])
    class Meta:
        db_table = u'tbl_talla'

class TblTipo(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    descripcion_tipo = models.CharField(max_length=30, help_text="Ejemplo: Bota", validators=[ValidarLetra])
    class Meta:
        db_table = u'tbl_tipo'

class TblProducto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    id_proveedor = models.ForeignKey(TblProveedor, db_column='id_proveedor')
    id_talla = models.ForeignKey(TblTalla, db_column='id_talla')
    id_color = models.ForeignKey(TblColor, db_column='id_color')
    id_tipo = models.ForeignKey(TblTipo, db_column='id_tipo')
    id_marca = models.ForeignKey(TblMarca, db_column='id_marca')
    id_estilo = models.ForeignKey(TblEstilo, db_column='id_estilo')
    descripcion_producto = models.CharField(max_length=75, help_text="Ejemplo: Detalle del Producto")
    precio_compra = models.DecimalField(max_digits=5, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=5, decimal_places=2)
    precio_minimo = models.DecimalField(max_digits=5, decimal_places=2)
    codigo_producto = models.CharField(max_length=12)
    codigo_existencia = models.CharField(max_length=21)
    class Meta:
        db_table = u'tbl_producto'
        
class TblDetalleEntrada(models.Model):
    id_detalle_entrada = models.AutoField(primary_key=True)
    id_entrada = models.ForeignKey(TblEntrada, db_column='id_entrada')
    id_producto = models.ForeignKey(TblProducto, db_column='id_producto')
    cantidad = models.IntegerField()
    class Meta:
        db_table = u'tbl_detalle_entrada'

class TblDetalleSalida(models.Model):
    id_detalle_salida = models.AutoField(primary_key=True)
    id_salida = models.ForeignKey(TblSalida, db_column='id_salida')
    id_producto = models.ForeignKey(TblProducto, db_column='id_producto')
    cantidad = models.IntegerField()
    class Meta:
        db_table = u'tbl_detalle_salida'