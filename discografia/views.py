from django.shortcuts import render

# Create your views here.
def discografia(request):
    contexto = {
        'titulo' : 'ABEBE BIKILA | Discografia'
    }
    return render(request, 
                  'discografia/index.html',
                  contexto)
