from argparse import Namespace
from django.urls import path, reverse
from .views import*
urlpatterns = [
    path('', home, name = 'index'),
    
    path('grupos/', grupos, name = 'grupos'),
    path('estadios/', estadios, name = 'estadios'),
    path('calendario/', calendario, name = 'calendario'),
    path('anfitriones/', anfitriones, name = 'anfitriones'),
    path('torneos/', torneos, name = 'torneos'),
    path('<slug:slug>/' ,detallePost, name = 'detalle_post'),
    
]
