from django.shortcuts import get_object_or_404, render

from .models import Categoria, Producto


def index(request):
    product_list = Producto.objects.select_related('categoria').order_by('nombre')[:6]
    categorias = Categoria.objects.order_by('nombre')
    context = {'product_list': product_list, 'categorias': categorias}
    return render(request, 'index.html', context)


def producto(request, producto_id):
    producto_item = get_object_or_404(
        Producto.objects.select_related('categoria'),
        pk=producto_id,
    )
    categorias = Categoria.objects.order_by('nombre')
    context = {'producto': producto_item, 'categorias': categorias}
    return render(request, 'producto.html', context)


def productos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    product_list = (
        Producto.objects.select_related('categoria')
        .filter(categoria=categoria)
        .order_by('nombre')
    )
    categorias = Categoria.objects.order_by('nombre')
    context = {
        'categoria_actual': categoria,
        'product_list': product_list,
        'categorias': categorias,
    }
    return render(request, 'categoria.html', context)
