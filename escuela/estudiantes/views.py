from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from estudiantes.models import Estudiante

# Create your views here.
def get_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/lista_estudiantes.html', {'estudiantes' : estudiantes})

def get_estudiante(request, estudiante_id):
    estudiante = Estudiante.objects.get(id=estudiante_id)
    return render(request, 'estudiantes/detalle.html', {'estudiante': estudiante})