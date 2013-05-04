from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from Zapateria.models import *
from Zapateria.forms import *
from django.contrib.auth.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def Acceso(request):
    Mensaje = ""
    if request.method == "POST":
        iFrmAcceso = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                Mensaje = "Verifica si tu Usuario esta Activo"
        else:
            Mensaje = "Usuario y/o Contrase&ntilde;a Incorrectos"
    else:
        iFrmAcceso = AuthenticationForm()
    return render_to_response("Acceso.html", {'iFrmAcceso':iFrmAcceso, 'Mensaje':Mensaje} , context_instance=RequestContext(request))

@login_required(login_url='/')
def Cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/')
def CambiarContra(request):
    if request.method == 'POST':
        iFrmContrasena = FrmContrasena(request.POST)
        if iFrmContrasena.is_valid():
            iUser = User.objects.get(username=request.user.username)
            iUser.set_password(request.POST['Nueva_Contrasena'])
            iUser.save()
            return HttpResponseRedirect('/')
    else:
        iFrmContrasena = FrmContrasena()
    return render_to_response("CambiarContrasena.html", {'iFrmContrasena':iFrmContrasena}, context_instance=RequestContext(request))

@permission_required('auth.Can add tbl salida', login_url='/')
def ConsultarZapateria(request):
    iTblZapateria = TblZapateria.objects.all()
    return render_to_response("ConsultarZapateria.html", {'iTblZapateria':iTblZapateria}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def AgregarZapateria(request):
    if request.method == 'POST':
        iFrmZapateria = FrmZapateria(request.POST)
        if iFrmZapateria.is_valid():
            iFrmZapateria.save()
            return HttpResponseRedirect('/Catalogo/Consultar/Zapateria/')
    else:
        iFrmZapateria = FrmZapateria()
    return render_to_response('AgregarZapateria.html', {'iFrmZapateria':iFrmZapateria}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def EditarZapateria(request, id_zapateria):
    iTblZapateria = TblZapateria.objects.get(pk=id_zapateria)
    if request.method == 'POST':
        iFrmZapateria = FrmZapateria(request.POST, instance=iTblZapateria)
        if iFrmZapateria.is_valid():
            iFrmZapateria.save()
            return HttpResponseRedirect('/Catalogo/Consultar/Zapateria/')
    else:
        iFrmZapateria = FrmZapateria(instance=iTblZapateria)
    return render_to_response('AgregarZapateria.html', {'iFrmZapateria':iFrmZapateria}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def EliminarZapateria(request, id_zapateria):
    iTblZapateria = TblZapateria.objects.get(pk=id_zapateria)
    iTblZapateria.delete()
    return HttpResponseRedirect('/Catalogo/Consultar/Zapateria/')

@permission_required('auth.Can add tbl salida', login_url='/')
def ConsultarTalla(request):
    iTblTalla = TblTalla.objects.all()
    return render_to_response("ConsultarTalla.html", {'iTblTalla':iTblTalla}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def AgregarTalla(request):
    if request.method == 'POST':
        iFrmTalla = FrmTalla(request.POST)
        if iFrmTalla.is_valid():
            iFrmTalla.save()
            return HttpResponseRedirect('/Catalogo/Consultar/Talla/')
    else:
        iFrmTalla = FrmTalla()
    return render_to_response('AgregarTalla.html', {'iFrmTalla':iFrmTalla}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def EditarTalla(request, id_talla):
    iTblTalla = TblTalla.objects.get(pk=id_talla)
    if request.method == 'POST':
        iFrmTalla = FrmTalla(request.POST, instance=iTblTalla)
        if iFrmTalla.is_valid():
            iFrmTalla.save()
            return HttpResponseRedirect('/Catalogo/Consultar/Talla/')
    else:
        iFrmTalla = FrmTalla(instance=iTblTalla)
    return render_to_response('AgregarTalla.html', {'iFrmTalla':iFrmTalla}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def EliminarTalla(request, id_talla):
    iTblTalla = TblTalla.objects.get(pk=id_talla)
    iTblTalla.delete()
    return HttpResponseRedirect('/Catalogo/Consultar/Talla/')

@permission_required('auth.Can add tbl salida', login_url='/')
def ConsultarColor(request):
    iTblColor = TblColor.objects.all()
    return render_to_response("ConsultarColor.html", {'iTblColor':iTblColor}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def AgregarColor(request):
    Mensaje = ""
    if request.method == 'POST':
        iFrmColor = FrmColor(request.POST)
        if iFrmColor.is_valid():
            try:
                iTblColor = TblColor.objects.get(descripcion_color=request.POST['descripcion_color'])
                Mensaje = "Color ya Existe"
                iFrmColor = FrmColor()
            except ObjectDoesNotExist, e:
                iFrmColor.save()
                return HttpResponseRedirect('/Catalogo/Consultar/Color/')
    else:
        iFrmColor = FrmColor()
    return render_to_response('AgregarColor.html', {'iFrmColor':iFrmColor, 'Mensaje':Mensaje}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def EditarColor(request, id_color):
    iTblColor = TblColor.objects.get(pk=id_color)
    if request.method == 'POST':
        iFrmColor = FrmColor(request.POST, instance=iTblColor)
        if iFrmColor.is_valid():
            iFrmColor.save()
            return HttpResponseRedirect('/Catalogo/Consultar/Color/')
    else:
        iFrmColor = FrmColor(instance=iTblColor)
    return render_to_response('EditarColor.html', {'iFrmColor':iFrmColor}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def EliminarColor(request, id_color):
    iTblColor = TblColor.objects.get(pk=id_color)
    iTblColor.delete()
    return HttpResponseRedirect('/Catalogo/Consultar/Color/')

@permission_required('auth.Can add tbl salida', login_url='/')
def ConsultarTipo(request):
    iTblTipo = TblTipo.objects.all()
    return render_to_response("ConsultarTipo.html", {'iTblTipo':iTblTipo}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def AgregarTipo(request):
    if request.method == 'POST':
        iFrmTipo = FrmTipo(request.POST)
        if iFrmTipo.is_valid():
            iFrmTipo.save()
            return HttpResponseRedirect('/Catalogo/Consultar/Tipo/')
    else:
        iFrmTipo = FrmTipo()
    return render_to_response('AgregarTipo.html', {'iFrmTipo':iFrmTipo}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def EditarTipo(request, id_tipo):
    iTblTipo = TblTipo.objects.get(pk=id_tipo)
    if request.method == 'POST':
        iFrmTipo = FrmTipo(request.POST, instance=iTblTipo)
        if iFrmTipo.is_valid():
            iFrmTipo.save()
            return HttpResponseRedirect('/Catalogo/Consultar/Tipo/')
    else:
        iFrmTipo = FrmTipo(instance=iTblTipo)
    return render_to_response('EditarTipo.html', {'iFrmTipo':iFrmTipo}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def EliminarTipo(request, id_estilo):
    iTblTipo = TblTipo.objects.get(pk=id_estilo)
    iTblTipo.delete()
    return HttpResponseRedirect('/Catalogo/Consultar/Tipo/')

@permission_required('auth.Can add tbl salida', login_url='/')
def ConsultarEstilo(request):
    iTblEstilo = TblEstilo.objects.all()
    return render_to_response("ConsultarEstilo.html", {'iTblEstilo':iTblEstilo}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def AgregarEstilo(request):
    if request.method == 'POST':
        iFrmEstilo = FrmEstilo(request.POST)
        if iFrmEstilo.is_valid():
            iFrmEstilo.save()
            return HttpResponseRedirect('/Catalogo/Consultar/Estilo/')
    else:
        iFrmEstilo = FrmEstilo()
    return render_to_response('AgregarEstilo.html', {'iFrmEstilo':iFrmEstilo}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def EditarEstilo(request, id_estilo):
    iTblEstilo = TblEstilo.objects.get(pk=id_estilo)
    if request.method == 'POST':
        iFrmEstilo = FrmEstilo(request.POST, instance=iTblEstilo)
        if iFrmEstilo.is_valid():
            iFrmEstilo.save()
            return HttpResponseRedirect('/Catalogo/Consultar/Estilo/')
    else:
        iFrmEstilo = FrmEstilo(instance=iTblEstilo)
    return render_to_response('EditarEstilo.html', {'iFrmEstilo':iFrmEstilo}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def EliminarEstilo(request, id_estilo):
    iTblEstilo = TblEstilo.objects.get(pk=id_estilo)
    iTblEstilo.delete()
    return HttpResponseRedirect('/Catalogo/Consultar/Estilo/')

@permission_required('auth.Can add tbl salida', login_url='/')
def ConsultarMarca(request):
    iTblMarca = TblMarca.objects.all()
    return render_to_response("ConsultarMarca.html", {'iTblMarca':iTblMarca}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def AgregarMarca(request):
    if request.method == 'POST':
        iFrmMarca = FrmMarca(request.POST)
        if iFrmMarca.is_valid():
            iFrmMarca.save()
            return HttpResponseRedirect('/Catalogo/Consultar/Marca/')
    else:
        iFrmMarca = FrmMarca()
    return render_to_response('AgregarMarca.html', {'iFrmMarca':iFrmMarca}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def EditarMarca(request, id_marca):
    iTblMarca = TblMarca.objects.get(pk=id_marca)
    if request.method == 'POST':
        iFrmMarca = FrmMarca(request.POST, instance=iTblMarca)
        if iFrmMarca.is_valid():
            iFrmMarca.save()
            return HttpResponseRedirect('/Catalogo/Consultar/Marca/')
    else:
        iFrmMarca = FrmMarca(instance=iTblMarca)
    return render_to_response('EditarMarca.html', {'iFrmMarca':iFrmMarca}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def EliminarMarca(request, id_marca):
    iTblMarca = TblMarca.objects.get(pk=id_marca)
    iTblMarca.delete()
    return HttpResponseRedirect('/Catalogo/Consultar/Marca/')

@permission_required('auth.Can add tbl salida', login_url='/')
def ConsultarProveedor(request):
    iTblProveedor = TblProveedor.objects.all()
    return render_to_response("ConsultarProveedor.html", {'iTblProveedor':iTblProveedor}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def AgregarProveedor(request):
    if request.method == 'POST':
        iFrmProveedor = FrmProveedor(request.POST)
        if iFrmProveedor.is_valid():
            iFrmProveedor.save()
            return HttpResponseRedirect('/Catalogo/Consultar/Proveedor/')
    else:
        iFrmProveedor = FrmProveedor()
    return render_to_response('AgregarProveedor.html', {'iFrmProveedor':iFrmProveedor}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def EditarProveedor(request, id_proveedor):
    iTblProveedor = TblProveedor.objects.get(pk=id_proveedor)
    if request.method == 'POST':
        iFrmProveedor = FrmProveedor(request.POST, instance=iTblProveedor)
        if iFrmProveedor.is_valid():
            iFrmProveedor.save()
            return HttpResponseRedirect('/Catalogo/Consultar/Proveedor/')
    else:
        iFrmProveedor = FrmProveedor(instance=iTblProveedor)
    return render_to_response('EditarProveedor.html', {'iFrmProveedor':iFrmProveedor}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def EliminarProveedor(request, id_proveedor):
    iTblProveedor = TblProveedor.objects.get(pk=id_proveedor)
    iTblProveedor.delete()
    return HttpResponseRedirect('/Catalogo/Consultar/Proveedor/')

@permission_required('auth.Can add tbl salida', login_url='/')
def ConsultarTipoEntrada(request):
    iTblTipoEntrada = TblTipoEntrada.objects.all()
    return render_to_response("ConsultarTipoEntrada.html", {'iTblTipoEntrada':iTblTipoEntrada}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def AgregarTipoEntrada(request):
    if request.method == 'POST':
        iFrmTipoEntrada = FrmTipoEntrada(request.POST)
        if iFrmTipoEntrada.is_valid():
            iFrmTipoEntrada.save()
            return HttpResponseRedirect('/Catalogo/Consultar/TipoEntrada/')
    else:
        iFrmTipoEntrada = FrmTipoEntrada()
    return render_to_response('AgregarTipoEntrada.html', {'iFrmTipoEntrada':iFrmTipoEntrada}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def EditarTipoEntrada(request, id_tipo_entrada):
    iTblTipoEntrada = TblTipoEntrada.objects.get(pk=id_tipo_entrada)
    if request.method == 'POST':
        iFrmTipoEntrada = FrmTipoEntrada(request.POST, instance=iTblTipoEntrada)
        if iFrmTipoEntrada.is_valid():
            iFrmTipoEntrada.save()
            return HttpResponseRedirect('/Catalogo/Consultar/TipoEntrada/')
    else:
        iFrmTipoEntrada = FrmTipoEntrada(instance=iTblTipoEntrada)
    return render_to_response('EditarTipoEntrada.html', {'iFrmTipoEntrada':iFrmTipoEntrada}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def EliminarTipoEntrada(request, id_tipo_entrada):
    iTblTipoEntrada = TblTipoEntrada.objects.get(pk=id_tipo_entrada)
    iTblTipoEntrada.delete()
    return HttpResponseRedirect('/Catalogo/Consultar/TipoEntrada/')

@permission_required('auth.Can add tbl salida', login_url='/')
def ConsultarTipoSalida(request):
    iTblTipoSalida = TblTipoSalida.objects.all()
    return render_to_response("ConsultarTipoSalida.html", {'iTblTipoSalida':iTblTipoSalida}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def AgregarTipoSalida(request):
    if request.method == 'POST':
        iFrmTipoSalida = FrmTipoSalida(request.POST)
        if iFrmTipoSalida.is_valid():
            iFrmTipoSalida.save()
            return HttpResponseRedirect('/Catalogo/Consultar/TipoSalida/')
    else:
        iFrmTipoSalida = FrmTipoSalida()
    return render_to_response('AgregarTipoSalida.html', {'iFrmTipoSalida':iFrmTipoSalida}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def EditarTipoSalida(request, id_tipo_salida):
    iTblTipoSalida = TblTipoSalida.objects.get(pk=id_tipo_salida)
    if request.method == 'POST':
        iFrmTipoSalida = FrmTipoSalida(request.POST, instance=iTblTipoSalida)
        if iFrmTipoSalida.is_valid():
            iFrmTipoSalida.save()
            return HttpResponseRedirect('/Catalogo/Consultar/TipoSalida/')
    else:
        iFrmTipoSalida = FrmTipoSalida(instance=iTblTipoSalida)
    return render_to_response('EditarTipoSalida.html', {'iFrmTipoSalida':iFrmTipoSalida}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def EliminarTipoSalida(request, id_tipo_salida):
    iTblTipoSalida = TblTipoSalida.objects.get(pk=id_tipo_salida)
    iTblTipoSalida.delete()
    return HttpResponseRedirect('/Catalogo/Consultar/TipoSalida/')

@permission_required('auth.Can add tbl salida', login_url='/')
def ConsultarCobrador(request):
    iTblPersonal = TblPersonal.objects.all()
    return render_to_response("ConsultarCobrador.html", {'iTblPersonal':iTblPersonal}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def AgregarCobrador(request):
    Mensaje = ""
    if request.method == 'POST':
        iFrmCobrador = FrmCobrador(request.POST)
        if iFrmCobrador.is_valid():
            try:
                iUser = User.objects.create_user(request.POST['Nombre_de_usuario'],
                                                 request.POST['correo_electronico_personal'],
                                                 request.POST['Contrasena'])
                iUser.save()
                idU = User.objects.latest('id')
                permiso = Permission.objects.get(name='Can add tbl salida')
                idU.user_permissions.add(permiso)
                NiFrmCobrador = iFrmCobrador.save(commit=False)
                NiFrmCobrador.user = idU
                idZ = TblZapateria.objects.get(pk=1)
                NiFrmCobrador.id_zapateria = idZ
                NiFrmCobrador.save()
                return HttpResponseRedirect('/Catalogo/Consultar/Cobrador/')
            except Exception as e:
                Mensaje = "Nombre de Usuario ya existe."
                iFrmCobrador = FrmCobrador()
    else:
        iFrmCobrador = FrmCobrador()
    return render_to_response('AgregarCobrador.html', {'iFrmCobrador':iFrmCobrador, 'Mensaje':Mensaje}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def EditarCobrador(request, id_personal):
    iTblPersonal = TblPersonal.objects.get(pk=id_personal)
    if request.method == 'POST':
        iFrmCobradorEditar = FrmCobradorEditar(request.POST, instance=iTblPersonal)
        if iFrmCobradorEditar.is_valid():
            iFrmCobradorEditar.save()
            return HttpResponseRedirect('/Catalogo/Consultar/Cobrador/')
    else:
        iFrmCobradorEditar = FrmCobradorEditar(instance=iTblPersonal)
    return render_to_response('EditarCobrador.html', {'iFrmCobradorEditar':iFrmCobradorEditar}, context_instance=RequestContext(request))
@permission_required('auth.Can add tbl salida', login_url='/')
def EliminarCobrador(request, id_personal):
    iTblPersonal = TblPersonal.objects.get(pk=id_personal)
    iUser = User.objects.get(pk=iTblPersonal.user_id)
    iUser.delete()
    iTblPersonal.delete()
    return HttpResponseRedirect('/Catalogo/Consultar/Cobrador/')