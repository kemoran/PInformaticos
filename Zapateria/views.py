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

