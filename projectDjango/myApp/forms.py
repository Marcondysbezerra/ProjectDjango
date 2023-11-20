from django import forms


class FormPortTest(forms.Form):
    ip_address_form = forms.GenericIPAddressField(protocol='ipv4')
    port_form = forms.IntegerField(min_value=0, max_value=65535)
