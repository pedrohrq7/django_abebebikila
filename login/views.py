from django.shortcuts import render
from login.models import Pessoa
# Create your views here.
def login(request):
    contexto = {
        'titulo' : 'ABEBE BIKILA | Cadastro',
        'pessoas': Pessoa.objects.all(),
    }
    return render(request, 
                  'login/index.html',
                  contexto)

def gravar(request):
    # salvar os dados da tela no banco
    nova_pessoa = Pessoa()
    nova_pessoa.nome     = request.POST.get("nome")
    nova_pessoa.telefone = request.POST.get("movel")
    nova_pessoa.email    = request.POST.get("correio")
    nova_pessoa.save()

    return login(request)

def editar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    return render(
        request,
        'login/index.html',
        {"pessoa": pessoa},
    )

def atualizar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    pessoa.nome = request.POST.get('nome')
    pessoa.telefone = request.POST.get('movel')
    pessoa.email = request.POST.get('correio')
    pessoa.save()
    return login(request)

def apagar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    pessoa.delete()
    return login(request)