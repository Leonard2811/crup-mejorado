from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Articulo
from .forms import ArticuloForm


def lista_articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'noticias/lista.html', {'articulos': articulos})


def detalle_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    return render(request, 'noticias/detalle.html', {'articulo': articulo})


@login_required
def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.autor = request.user
            articulo.save()
            messages.success(request, '¡Artículo creado exitosamente!')
            return redirect('detalle_articulo', pk=articulo.pk)
    else:
        form = ArticuloForm()
    return render(request, 'noticias/crear.html', {'form': form})


@login_required
def editar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if articulo.autor != request.user:
        messages.error(request, 'No tienes permiso para editar este artículo.')
        return redirect('detalle_articulo', pk=pk)
    if request.method == 'POST':
        form = ArticuloForm(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Artículo actualizado exitosamente!')
            return redirect('detalle_articulo', pk=articulo.pk)
    else:
        form = ArticuloForm(instance=articulo)
    return render(request, 'noticias/editar.html', {'form': form, 'articulo': articulo})


@login_required
def eliminar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if articulo.autor != request.user:
        messages.error(request, 'No tienes permiso para eliminar este artículo.')
        return redirect('detalle_articulo', pk=pk)
    if request.method == 'POST':
        articulo.delete()
        messages.success(request, 'Artículo eliminado.')
        return redirect('lista_articulos')
    return render(request, 'noticias/confirmar_eliminar.html', {'articulo': articulo})
