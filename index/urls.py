from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('perfil/', views.perfil, name='perfil'),
    path('buscar/', views.buscar, name='buscar'),
    path('registro/', views.registro, name='registro'),
    path('mensajes/', views.mensajes, name='mensajes'),
    path('admin/', views.admin, name='admin'),
    path('musico/<str:pk>', views.ConsultarMusico.as_view(), name='consultar_musico'),
    path('mensaje/<str:pk>', views.ConsultarMensaje.as_view(), name='consultar_mensaje'),
    
]

urlpatterns+=[
    path('musico/create/', views.CrearMusico.as_view(), name='crear_musico'),
    path('musico/<str:pk>/update/', views.ActualizarMusico.as_view(), name='actualizar_musico'),
    path('musico/<str:pk>/delete/', views.EliminarMusico.as_view(), name='eliminar_musico'),

    path('mensaje/create/', views.CrearMensaje.as_view(), name='crear_mensaje'),
    path('mensaje/<str:pk>/update/', views.ActualizarMensaje.as_view(), name='actualizar_mensaje'),
    path('mensaje/<str:pk>/delete/', views.EliminarMensaje.as_view(), name='eliminar_mensaje'),
    
    

]