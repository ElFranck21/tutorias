from django.contrib import admin

from .models import seguimiento

@admin.register(seguimiento)
class seguimientoAdmin(admin.ModelAdmin):
    fields=('period','career','tutor','semester','group','student')


# Register your models here.
