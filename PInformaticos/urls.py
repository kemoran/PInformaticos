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
    
    url(r'^Catalogo/Consultar/Talla/$','Zapateria.views.ConsultarTalla'),
    url(r'^Catalogo/Agregar/Talla/$','Zapateria.views.AgregarTalla'),
    url(r'^Catalogo/Editar/Talla/(?P<id_talla>\d+)/$','Zapateria.views.EditarTalla'),
    url(r'^Catalogo/Eliminar/Talla/(?P<id_talla>\d+)/$','Zapateria.views.EliminarTalla'),
    
    url(r'^Catalogo/Consultar/Color/$','Zapateria.views.ConsultarColor'),
    url(r'^Catalogo/Agregar/Color/$','Zapateria.views.AgregarColor'),
    url(r'^Catalogo/Editar/Color/(?P<id_color>\d+)/$','Zapateria.views.EditarColor'),
    url(r'^Catalogo/Eliminar/Color/(?P<id_color>\d+)/$','Zapateria.views.EliminarColor'),
    
    url(r'^Catalogo/Consultar/Tipo/$','Zapateria.views.ConsultarTipo'),
    url(r'^Catalogo/Agregar/Tipo/$','Zapateria.views.AgregarTipo'),
    url(r'^Catalogo/Editar/Tipo/(?P<id_tipo>\d+)/$','Zapateria.views.EditarTipo'),
    url(r'^Catalogo/Eliminar/Tipo/(?P<id_tipo>\d+)/$','Zapateria.views.EliminarTipo'),
    
    url(r'^Catalogo/Consultar/Estilo/$','Zapateria.views.ConsultarEstilo'),
    url(r'^Catalogo/Agregar/Estilo/$','Zapateria.views.AgregarEstilo'),
    url(r'^Catalogo/Editar/Estilo/(?P<id_estilo>\d+)/$','Zapateria.views.EditarEstilo'),
    url(r'^Catalogo/Eliminar/Estilo/(?P<id_estilo>\d+)/$','Zapateria.views.EliminarEstilo'),
    
    url(r'^Catalogo/Consultar/Marca/$','Zapateria.views.ConsultarMarca'),
    url(r'^Catalogo/Agregar/Marca/$','Zapateria.views.AgregarMarca'),
    url(r'^Catalogo/Editar/Marca/(?P<id_marca>\d+)/$','Zapateria.views.EditarMarca'),
    url(r'^Catalogo/Eliminar/Marca/(?P<id_marca>\d+)/$','Zapateria.views.EliminarMarca'),
    
    url(r'^Catalogo/Consultar/Proveedor/$','Zapateria.views.ConsultarProveedor'),
    url(r'^Catalogo/Agregar/Proveedor/$','Zapateria.views.AgregarProveedor'),
    url(r'^Catalogo/Editar/Proveedor/(?P<id_proveedor>\d+)/$','Zapateria.views.EditarProveedor'),
    url(r'^Catalogo/Eliminar/Proveedor/(?P<id_proveedor>\d+)/$','Zapateria.views.EliminarProveedor'),
    
    url(r'^Catalogo/Consultar/TipoEntrada/$','Zapateria.views.ConsultarTipoEntrada'),
    url(r'^Catalogo/Agregar/TipoEntrada/$','Zapateria.views.AgregarTipoEntrada'),
    url(r'^Catalogo/Editar/TipoEntrada/(?P<id_tipo_entrada>\d+)/$','Zapateria.views.EditarTipoEntrada'),
    url(r'^Catalogo/Eliminar/TipoEntrada/(?P<id_tipo_entrada>\d+)/$','Zapateria.views.EliminarTipoEntrada'),
    
    url(r'^Catalogo/Consultar/TipoSalida/$','Zapateria.views.ConsultarTipoSalida'),
    url(r'^Catalogo/Agregar/TipoSalida/$','Zapateria.views.AgregarTipoSalida'),
    url(r'^Catalogo/Editar/TipoSalida/(?P<id_tipo_salida>\d+)/$','Zapateria.views.EditarTipoSalida'),
    url(r'^Catalogo/Eliminar/TipoSalida/(?P<id_tipo_salida>\d+)/$','Zapateria.views.EliminarTipoSalida'),
    
)
