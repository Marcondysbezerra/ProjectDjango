from django import forms


class FormPortTest(forms.Form):
    ip_address_form = forms.GenericIPAddressField()
    port_form = forms.IntegerField(min_value=0, max_value=65535)

    def __init__(self, *args, **kwargs):
        super(FormPortTest, self).__init__(*args, **kwargs)
        self.fields['ip_address_form'].label = 'Host:'
        self.fields['port_form'].label = 'Porta:'
