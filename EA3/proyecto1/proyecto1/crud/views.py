from django.shortcuts import render

# Create your views here.
def categoria(request):
    contexto = {}
    if request.method == 'POST':
        id      = request.POST["txtId"]
        nombre  = request.POST["txtNombre"]
        #activo  = request.POST["chkActivo"]
        
        if 'btnGuardar' in request.POST:
            # orm ??? django
            contexto = {'btn': 'guardar'}
        elif 'btnListar' in request.POST:
            contexto = {'btn': 'btnListar'}
        elif 'btnEliminar' in request.POST:
            contexto = {'btn': 'btnEliminar'}
        elif 'btnListar' in request.POST:
            contexto = {'btn': 'btnListar'}

    return render(request, 'categoria.html', contexto)

def marca(request):

    return render(request, 'marca.html', {})


