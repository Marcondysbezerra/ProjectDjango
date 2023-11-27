from django import forms


class FormPortTest(forms.Form):
    ip_address_form = forms.GenericIPAddressField(protocol='ipv4')
    port_form = forms.IntegerField(min_value=0, max_value=65535)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["ip_address_form"].widget.attrs.update({"class": "form-control"})
        self.fields["port_form"].widget.attrs.update({"class": "form-control"})
