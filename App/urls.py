from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('cartas/', cartas, name='Cartas'),
    path('torneo/', torneo, name='torneo'),
    path('crear-torneo/', crearTorneo, name='crearTorneo'),
    path('eliminar-torneo/<int:id>', eliminarTorneo, name='eliminarTorneo'),
    path('edita-torneo/<int:id>', editarTorneo, name='editarTorneo'),
    path('contactenos/', contactenos, name='Contactenos'),
    path('about/', about, name='About'),
]
