import socket
import os
from requests import get
from django.conf import settings
from django.shortcuts import render, HttpResponse
from projectDjango.myApp.forms import FormPortTest


def pagina_inicial(request):
    result = ''
    erro = ''

    if request.method == "POST":
        form = FormPortTest(request.POST)
        if form.is_valid():
            host = form.cleaned_data['ip_address_form']
            port = form.cleaned_data['port_form']

            connection = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
            connection.settimeout(1)

            try:
                result = connection.connect_ex((host, port))
            except socket.gaierror as e:
                erro = e

            connection.close()

            context = {
                'form': form,
                'result': result,
                'host': host,
                'port': port,
                'erro': erro,
            }

            return render(request, 'ipv4/index.html', context=context)

    else:
        form = FormPortTest()
    return render(request, "ipv4/index.html", {"form": form})


def your_ip(request):
    ip = get('https://api.ipify.org').text
    context = {'ip': ip}
    return render(request, 'ipv4/meuip.html', context=context)


def teste_ipv4(request):
    result = ''
    erro = ''

    if request.method == "POST":
        form = FormPortTest(request.POST)
        if form.is_valid():
            host = form.cleaned_data['ip_address_form']
            port = form.cleaned_data['port_form']

            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.settimeout(1)

            try:
                result = connection.connect_ex((host, port))
            except socket.gaierror as e:
                erro = e

            connection.close()

            context = {
                'form': form,
                'result': result,
                'host': host,
                'port': port,
                'erro': erro,
            }

            return render(request, 'ipv4/prot.html', context=context)
    else:
        form = FormPortTest()
    return render(request, "ipv4/prot.html", {"form": form})

"""def robots(request):
    if not settings.DEBUG:
        pass
    else:
        path = os.path.join(settings.BASE_DIR, 'templates/static/robots.txt')
    with open(path, 'r') as arq:
        return HttpResponse(arq)"""