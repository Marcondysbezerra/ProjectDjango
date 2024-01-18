from django.urls import path
from . import views


urlpatterns = [
    path('', views.teste_ipv4),
    path('teste-ipv4/', views.teste_ipv4),
    path('meuip/', views.your_ip),

]
