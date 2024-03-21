from django.urls import path 
from . import views

urlpatterns = [
    # cuando accedamos al directorio raiz (''), nos retornamos a una vista
    path('', views.home),
    path('registrarPersona/', views.registrarPersona),
    path('edicionPersona/<dni>', views.edicionPersona),
    path('editarPersona/', views.editarPersona),
    path('eliminarPersona/<dni>', views.eliminarPersona)
]
