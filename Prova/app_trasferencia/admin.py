from django.contrib import admin
from .models import Trasferencia, ContadorTrasferencia

class ListaTrasferencias(admin.ModelAdmin):
    list_display= ('conta',)
    list_display_links= ('conta',)

admin.site.register(Trasferencia,ListaTrasferencias)
admin.site.register(ContadorTrasferencia)