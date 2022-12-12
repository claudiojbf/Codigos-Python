from django.contrib import admin
from .models import Deposito,ContadorDeposito

class ListaDeposito(admin.ModelAdmin):
    list_display= ('conta',)
    list_display_links= ('conta',)

admin.site.register(Deposito, ListaDeposito)
admin.site.register(ContadorDeposito)
