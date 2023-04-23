from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *
from django.views.generic import ListView
# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def cartas(request):
    return render(request, 'cartas.html')


#CRUD Torneo

#Read Torneo
def torneo(request):

    torneo = Torneo.objects.all()   

    return render(request, 'torneo.html', {"torneo": torneo})


# Create Torneo
def crearTorneo(request):
    if request.method == 'POST':
        miFormulario = TorneoFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            dataformulario = miFormulario.cleaned_data
            inscripcion = Torneo(nombre_torneo = dataformulario['nombre_torneo'],
                                 cantidad_participantes = dataformulario['cantidad_participantes'], 
                                 lugar_del_torneo = dataformulario['lugar_del_torneo'], 
                                 premio = dataformulario['premio'], 
                                 codigo_de_torneo = dataformulario['codigo_de_torneo'], 
                                 imagen = dataformulario['imagen']
                                 )
            inscripcion.save()
            return redirect(reverse('Inicio'))
        else:
            return render(request, 'cartas.html',{"mensaje":"Formulario Invalido"})

    else:
        miFormulario = TorneoFormulario()
        return render(request, 'crear-torneo.html', {'miFormulario': miFormulario})
    
#Delete Torneo

def eliminarTorneo(request, id):
    if request.method == 'POST':

        torneo = Torneo.objects.get(id=id)
        torneo.delete()

        torneos = Torneo.objects.all()
        return render(request, 'eliminartorneo.html', {"torneos":torneos} )

#Update Torneo

def editarTorneo(request, id):

    torneo = Torneo.objects.get(id=id)
    
    if request.method == 'POST':
        miFormulario = TorneoFormulario(request.POST)
        if miFormulario.is_valid():
            dataformulario = miFormulario.cleaned_data
            torneo.nombre_torneo = dataformulario['nombre_torneo']
            torneo.cantidad_participantes = dataformulario['cantidad_participantes']
            torneo.lugar_del_torneo = dataformulario['lugar_del_torneo']
            torneo.premio = dataformulario['premio']
            torneo.codigo_de_torneo = dataformulario['codigo_de_torneo']
            torneo.imagen = dataformulario['imagen']
            torneo.save()
            return redirect(reverse('Inicio'))
        else:
            return render(request, 'torneo.html',{"mensaje":"Formulario Invalido"})

    else:
        miFormulario = TorneoFormulario(initial={
            "nombre":torneo.nombre_torneo,
            "cantidad":torneo.cantidad_participantes,
            "Lugar":torneo.lugar_del_torneo,
            "Premio": torneo.premio,    
            "Codigo":torneo.codigo_de_torneo,
            "Imagen": torneo.imagen
        })
        return render(request, 'editar-torneo.html', {'miFormulario': miFormulario})


def contactenos(request):
    return render(request, 'contactenos.html')

def about(request):
    return render(request, 'acerca_de_mi.html')

