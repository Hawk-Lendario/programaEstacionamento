from django.shortcuts import render
from .models import Contato


# Create your views here.
def home(request):
    return render(request, 'website/index.html')


def contato(request):
    mensagem = ''
    if request.method == 'POST':
        try:
            contatos = {}
            contatos['email'] = request.POST.get('email')
            contatos['nome'] = request.POST.get('nome')
            contatos['sobrenome'] = request.POST.get('sobrenome')
            contatos['endereco'] = request.POST.get('endereco')
            contatos['receber_noticias'] = True if request.POST.get('receber_noticias') == 'on' else False
            contatos['mensagem'] = request.POST.get('mensagem')

            Contato.objects.create(**contatos)
        except Exception as e:
            mensagem = str(e)
        else:
            mensagem = 'Contato realizado com sucesso'

    return render(request, 'website/contato.html', {'mensagem': mensagem})


def servicos(request):
    return render(request, 'website/servicos.html')


def sobre(request):
    return render(request, 'website/sobre.html')


def planos(request):
    return render(request, 'website/planos.html')
