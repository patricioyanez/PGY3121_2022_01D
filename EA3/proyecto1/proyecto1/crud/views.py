from django.shortcuts import redirect, render
from crud.models import Categoria
# Create your views here.
def categoria(request):
    contexto = {}
    ## utilizaremos el ORM de Django
    if request.method == 'POST':
        # captura de datos, obtenidos desde el formulario (plantilla)
        id      = int("0" + request.POST["txtId"])
        nombre  = request.POST["txtNombre"]    
        activo  = False
        if 'chkActivo' in request.POST:
            activo  = True
        print(request.POST)
        if 'btnGuardar' in request.POST: # detecta si el guardar fue presionado
            if id < 1:
                Categoria.objects.create(nombre= nombre, activo = activo)
            else:
                item = Categoria.objects.get(pk = id) # busca 1 elemento que coincida con el pk o id
                item.nombre = nombre
                item.activo = activo
                item.save()
            contexto = {'mensaje': 'guardado con éxito'}
        elif 'btnListar' in request.POST:
            listado = Categoria.objects.all() # devuelve todos los elementos guardados en la base de datos
            contexto = {'listado': listado}
        elif 'btnEliminar' in request.POST:
            item = Categoria.objects.get(pk = id) # busca 1 elemento que coincida con el pk o id
            item.delete()

            contexto = {'mensaje': item.nombre + ' fue eliminado con éxito'} 
    return render(request, 'categoria.html', contexto)


def categoriaLeer(request,buscarId):
    contexto = { }
    if not buscarId is None:
        item = Categoria.objects.get(pk= buscarId)
        contexto = {'item': item }
    return render(request, 'categoria.html', contexto)



def marca(request):
    return render(request, 'marca.html', {})


