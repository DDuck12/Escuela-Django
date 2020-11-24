"""escuela URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from estudiantes.views import get_estudiantes
from clases.views import get_clases
from clases.views import get_clase
from estudiantes.views import get_estudiante

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estudiantes/', get_estudiantes),
    path('clases/', get_clases),
    path('clases/<clase_id>', get_clase),
    path('estudiantes/<estudiante_id>', get_estudiante),
]
