from django.urls import path
from . import views


urlpatterns = [
    path('teste_ipv4', views.pagina_inicial, name='teste_ipv4')
]