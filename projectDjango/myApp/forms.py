from django.core.exceptions import ValidationError
from django.core.validators import validate_ipv4_address
from django import forms


def validacao_ipv4(valor):
    try:
        validate_ipv4_address(valor)
    except ValidationError:
        msg_error = {'invalid': 'Insira um endereço IP válido!'}


class FormPortTest(forms.Form):
    ip_address_form = forms.GenericIPAddressField(protocol='IPv4', validators=[validacao_ipv4])
    port_form = forms.IntegerField(min_value=0, max_value=65535)
