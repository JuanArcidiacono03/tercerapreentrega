from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.
def home(request):
    return render(request, "aplicacion/index.html")
    

def equipos(request):
    contexto = {'equipo': Equipo.objects.all()} 
    return render(request, "aplicacion/equipos.html",contexto )

def posiciones(request):
    contexto = {'posicion': Posicion.objects.all()}
    return render(request, "aplicacion/posiciones.html",contexto)  

def goleadores(request):
    contexto = {'goleador': Goleador.objects.all()}
    return render(request, "aplicacion/goleadores.html", contexto)



#________________Forms

def equipoForm(request):
    if request.method == "POST":
        miForm = EquipoForm(request.POST)
        if miForm.is_valid():
            equipo_nombre = miForm.cleaned_data.get("nombre")
            equipo = Equipo(nombre=equipo_nombre)
            equipo.save()
           
            contexto = {'equipo': Equipo.objects.all()} 
            return render(request, "aplicacion/equipos.html",contexto )


    else: 
          miForm = EquipoForm() 
    return render(request, "aplicacion/equipoForm.html", {"form": miForm})

def goleadorForm(request):
    if request.method == "POST":
        miForm = GoleadorForm(request.POST)
        if miForm.is_valid():
            goleador_nombre = miForm.cleaned_data.get("nombre")
            goleador = Goleador(nombre=goleador_nombre)
                                
            goleador.save()
           
            contexto = {'goleador': Goleador.objects.all()} 
            return render(request, "aplicacion/goleadores.html",contexto )


    else: 
          miForm = GoleadorForm() 
    return render(request, "aplicacion/goleadorForm.html", {"form": miForm})



def buscarEquipo(request):
    return render(request, "aplicacion/buscar_Equipo.html")

def encontrarEquipo(request):
    if request.GET ["buscar"]:
       patron = request.GET ["buscar"]
       equipos = Equipo.objects.filter(nombre__icontains=patron)
       contexto = {"equipos": equipos}
       
       return render(request, "aplicacion/buscar_equipo.html", contexto)
           
    return render(request, "aplicacion/buscar_equipo.html")


