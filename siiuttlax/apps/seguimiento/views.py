from django.shortcuts import render
from apps.academy.models import Student
from .models import Career  # Asegúrate de importar el modelo Career

def seguimiento(request):
    careers = Career.objects.all()  # Obtén todas las carreras
    students = Student.objects.all()  # Obtén todos los estudiantes
    return render(request, 'seguimiento/seguimiento.html', {'careers': careers, 'students': students})
