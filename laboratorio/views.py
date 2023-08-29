from django.shortcuts import render, redirect
from laboratorio.models import Laboratorio
from laboratorio.forms import LaboratorioForm


def index(request):
    context = {}
    return render(request, 'index.html', context)


def listar_lab(request):
    
    numvisit = request.session.get('numvisit', 0)
    numvisit += 1
    request.session['numvisit'] = numvisit
    
    laboratorios = Laboratorio.objects.all()
    
    context = {
        'laboratorios': laboratorios,
        'numvisit': numvisit,
    }
    
    return render(request, 'list.html', context)


def insertar_lab(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_lab')
    else:
        form = LaboratorioForm()

    context = {
        'form': form
    }
    
    return render(request, 'create.html', context)


def editar_lab(request, laboratorio_id):
    laboratorio = Laboratorio.objects.get(id=laboratorio_id)

    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('listar_lab')
    else:
        form = LaboratorioForm(instance=laboratorio)
    
    context = {
        'form': form
    }
    
    return render(request, 'update.html', context)


def eliminar_lab(request, laboratorio_id):
    laboratorio = Laboratorio.objects.get(id=laboratorio_id)

    if request.method == 'POST':
        confirmacion = request.POST.get('confirmacion')
        if confirmacion == 'si':
            laboratorio.delete()
            return redirect('listar_lab')
        else:
            return redirect('listar_lab') 
    
    context = {
        'laboratorio': laboratorio,
    }
    
    return render(request, 'delete.html', context)