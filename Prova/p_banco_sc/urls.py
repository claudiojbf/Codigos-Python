from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_conta.urls')),
    path('cliente', include('app_cliente.urls')),
    path('deposito', include('app_deposito.urls')),
    path('trasferencia', include('app_trasferencia.urls')),
]
