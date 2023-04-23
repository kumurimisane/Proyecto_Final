from django import forms
from .models import *

class CartasFormulario(forms.ModelForm):
    class Meta:
        model = Cartas
        fields = ['nombre', 'tipo', 'nivel','ataque', 'defensa','descripcion','imagen']

class MazoFormulario(forms.ModelForm):
    class Meta:
        model = Mazo
        fields = ['nombre', 'tipo', 'carta_principal', 'cantidad_de_cartas', 'descripcion','imagen']

class TorneoFormulario(forms.ModelForm):
    class Meta:
        model = Torneo
        fields = ['nombre_torneo', 'cantidad_participantes', 'lugar_del_torneo', 'premio', 'codigo_de_torneo', 'imagen']

class ContactoFormulario(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'apellido', 'email', 'mensaje']

