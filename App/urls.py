from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('cartas/', cartas, name='Cartas'),
    path('crear-cartas/', crearCartas, name='crearCartas'),
    path('eliminar-cartas/<int:id>', eliminarCartas, name='eliminarCartas'),
    path('edita-cartas/<int:id>', editarCartas, name='editarCartas'),
    path('torneo/', torneo, name='torneo'),
    path('crear-torneo/', crearTorneo, name='crearTorneo'),
    path('eliminar-torneo/<int:id>', eliminarTorneo, name='eliminarTorneo'),
    path('edita-torneo/<int:id>', editarTorneo, name='editarTorneo'),
    path('mazos/', MazoList.as_view(), name='Mazos'),
    path('mazos-detail/', MazoDetail.as_view(), name='mazoDeteail'),
    path('mazos-create/', MazoCreate.as_view(), name='crearMazo'),
    path('mazos-update/<int:pk>', MazoUpdate.as_view(), name='editarMazo'),
    path('mazos-delete/<int:pk>', MazoDelete.as_view(), name='eliminarMazo'),
    path('contactenos/', contactenos, name='Contactenos'),
    path('about/', about, name='About'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)