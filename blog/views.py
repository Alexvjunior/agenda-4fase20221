from django.shortcuts import render
from django.http import HttpResponse
from blog.forrms import ContatoForm
from django.template.loader import render_to_string

from blog.models import Contato

def index(request):
    contatos = Contato.objects.all()
    if request.method == "POST":
        form = ContatoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ContatoForm()
    return render(request, 'index.html', {"contatos": contatos, "form":form})

def index_contato(request, contato_id):
    contato = Contato.objects.filter(id=contato_id).first()
    return render(request, 'contato_index.html', {"contato": contato})
