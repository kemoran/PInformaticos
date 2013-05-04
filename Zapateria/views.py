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