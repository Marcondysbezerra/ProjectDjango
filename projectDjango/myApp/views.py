import socket
from django.shortcuts import render
from projectDjango.myApp.forms import FormPortTest


# Create your views here.
def pagina_inicial(request):

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = FormPortTest(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            host = form.cleaned_data['ip_address_form']
            port = form.cleaned_data['port_form']

            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.settimeout(1)
            result = connection.connect_ex((host, port))
            # connection.close()

            context = {
                'form': form,
                'result': result,
                'host': host,
                'port': port,
            }
            # redirect to a new URL:
            return render(request, 'ipv4/index.html', context=context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FormPortTest()
    return render(request, "ipv4/index.html", {"form": form})