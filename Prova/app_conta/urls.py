from django.urls import path
from . import views

urlpatterns = [
    path('inicio/<int:id>', views.conta, name = 'conta'),
]