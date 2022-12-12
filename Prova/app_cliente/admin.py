from django.contrib import admin
from .models import Cliente

class ListandoCliente(admin.ModelAdmin):
    list_display= ('id','nome')
    list_display_links= ('id','nome')

admin.site.register(Cliente, ListandoCliente)