from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages

# Create your views here.
def asignaturas(request):
    listaUsuarios = Usuario.objects.all()
    messages.success(request, 'Cursos listados')
    return render(request, "gestionUsuarios.html", {"usuarios": listaUsuarios})

def inicio(request):
    return render(request, "inicio.html")

def registrarUsuario(request): 
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']

    usuario=Usuario.objects.create(codigo=codigo, nombre=nombre, apellido=apellido)
    messages.success(request, 'Asignatura registrado')
    return redirect('/')

def eliminarUsuario(request, codigo):
    usuario = Usuario.objects.get(codigo=codigo)
    usuario.delete()
    messages.success(request, 'Asignatura eliminado')

    return redirect('/')

def edicionUsuario(request,codigo):
    usuario = Usuario.objects.get(codigo=codigo)
    return render(request, "edicionUsuarios.html", {"usuario":usuario})

def editarUsuario(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']

    usuario = Usuario.objects.get(codigo=codigo)
    usuario.nombre = nombre
    usuario.apellido = apellido
    usuario.save()
    messages.success(request, 'Asignatura modificado')

    return redirect('/')
