from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name = 'index'),
    path('generales/',generales, name = 'generales'),
    path('programacion/',programacion, name = 'programacion'),
    path('tutoriales/',tutoriales, name = 'tutoriales'),
    path('tecnologia/',tecnologia, name = 'tecnologia'),
    path('videojuegos/',videojuegos, name = 'videojuegos'),
    path('<slug:slug>/', detallePost, name='detalle_post'),
]
