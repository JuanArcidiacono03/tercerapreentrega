from django.urls import path, include
from.views import *


urlpatterns = [
    path('', home, name = "home"),
    path('equipos', equipos, name = "equipos"),
    path('posiciones', posiciones, name = "posiciones"),
    path('goleadores', goleadores, name = "goleadores"),
    
    path('equipo_form', equipoForm, name = "equipo_form"),
    
    path('goleador_form', goleadorForm, name = "goleador_form"),
    
    path('buscar_equipo', buscarEquipo, name = "buscar_equipo"),
    path('encontrar_equipo', encontrarEquipo, name = "encontrar_equipo"),
    
    
]
