from django.db import models

from apps.period.models import Semester,Period
from apps.group.models import Group
from apps.career.models import Career
from apps.academy.models import Professor,Student
# Create your models here.
class seguimiento(models.Model):
    period = models.ForeignKey(
        Period, 
        on_delete=models.CASCADE,
        verbose_name='Periodo')
    
    


    career= models.ForeignKey(
        Career, 
        on_delete=models.CASCADE,
        verbose_name='Carrera')
    
    tutor= models.ForeignKey(
        Professor, 
        on_delete=models.CASCADE, 
        verbose_name='Tutor',
        null=True, blank=True)
    
    semester = models.ForeignKey(
        Semester, 
        on_delete=models.CASCADE, 
        default=1, 
        verbose_name='Cuatrimestre')

    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE, 
        default=1, 
        verbose_name='Grupo'
    )

    student=models.ForeignKey(
        Student,
        on_delete=models.CASCADE, 
        verbose_name='Estudiante',
        null=True, blank=True)
    

        