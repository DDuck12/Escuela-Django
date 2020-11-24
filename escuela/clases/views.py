from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from clases.models import Clase


# Create your views here.
def get_clases(request):
    clases = Clase.objects.all()
    return render(request, 'clases/lista_clases.html', {'clases' : clases})

def get_clase(request, clase_id):
    clase = get_object_or_404(Clase, id=clase_id)
    return render(request, 'clases/detalle.html', {'clase': clase, 'estudiantes': clase.estudiantes.all()})