from django.shortcuts import render

# Create your views here.
def login(request):
    contexto = {
        'titulo' : 'ABEBE BIKILA | Login'
    }
    return render(request, 
                  'login/index.html',
                  contexto)