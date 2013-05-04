from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PInformaticos.views.home', name='home'),
    # url(r'^PInformaticos/', include('PInformaticos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'Zapateria.views.Acceso'),
    
    url(r'^Cerrar/$','Zapateria.views.Cerrar'),
    url(r'^Usuario/Contrasena/$','Zapateria.views.CambiarContra'),
    
    url(r'^Catalogo/Consultar/Zapateria/$','Zapateria.views.ConsultarZapateria'),
    url(r'^Catalogo/Agregar/Zapateria/$','Zapateria.views.AgregarZapateria'),
    url(r'^Catalogo/Editar/Zapateria/(?P<id_zapateria>\d+)/$','Zapateria.views.EditarZapateria'),
    url(r'^Catalogo/Eliminar/Zapateria/(?P<id_zapateria>\d+)/$','Zapateria.views.EliminarZapateria'),
    
    
)
