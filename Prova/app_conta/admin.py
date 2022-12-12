from django.contrib import admin
from .models import Conta

class ListaConta(admin.ModelAdmin):
    list_display= ('usuario',)
    list_display_links= ('usuario',)

admin.site.register(Conta, ListaConta)