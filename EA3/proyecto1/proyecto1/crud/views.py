from django.shortcuts import render

# Create your views here.
def categoria(request):
    return render(request, 'categoria.html', {'nombre': 'Ana'})

def marca(request):
    return render(request, 'marca.html', {})


