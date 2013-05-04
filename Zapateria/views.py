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