from django.db import models

class Contato(models.Model):

    name = models.CharField(max_length=50)

    email = models.EmailField()

    telefone = models.CharField(max_length=30)

    data_criacao = models.DateField(default=None, null=True)

