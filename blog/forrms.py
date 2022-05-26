import imp
from django import forms
from blog import models


class ContatoForm(forms.ModelForm):
    class Meta:
        model = models.Contato
        fields = ("__all__")