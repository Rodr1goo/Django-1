from django.shortcuts import render, redirect
from .models import Usuario

# Create your views here.

def home(request):
    usuarios = Usuario.objects.all()
    return render(request, "gestion.html", {"usuarios": usuarios})




def registrarPersona(request):
    dni=request.POST['numDni']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']
    materia=request.POST['txtMateria']
    
    usuario = Usuario.objects.create(dni=dni, nombre=nombre, apellido=apellido, materia=materia)

    return redirect('/')





def edicionPersona(request, dni):
    usuario = Usuario.objects.get(dni=dni)
    return render(request, "edicionPersona.html", {"usuario":usuario})

def editarPersona(request):
    dni=request.POST['numDni']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']
    materia=request.POST['txtMateria']

    usuario = Usuario.objects.get(dni=dni)
    usuario.nombre = nombre
    usuario.apellido = apellido
    usuario.materia = materia
    usuario.save()

    return redirect('/')




def eliminarPersona(request, dni):
    usuario = Usuario.objects.get(dni=dni)
    usuario.delete()

    return redirect('/')