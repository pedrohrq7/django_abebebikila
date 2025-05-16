from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def cadastro(request):
    # Se o usuário já estiver autenticado, redireciona para a página inicial
    if request.user.is_authenticated:
        return redirect('pagina_inicial')  # Altere para o nome da sua URL inicial
    
    contexto = {
        'titulo': 'ABEBE BIKILA | Login'
    }
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('pagina_inicial')  # Altere para o nome da sua URL inicial
        else:
            messages.error(request, 'Usuário ou senha incorretos!')
            return render(request, 'cadastro/index.html', contexto)
    
    return render(request, 'cadastro/index.html', contexto)

def logout_view(request):
    logout(request)
    return redirect('cadastro')  # Redireciona para a página de login após logout