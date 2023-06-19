from django.shortcuts import render, get_object_or_404, redirect
from ..models import Usuario, Emprestimo, Reserva, Equipamento
import os
import uuid
import shutil

from django.urls import reverse

from django.core.paginator import Paginator

def editar_equipamento(request, equipamento_id):
    equipamento = get_object_or_404(Equipamento, pk=equipamento_id)
    page_title = 'Equipamento - Detalhes'
    breadcrumb = [
        {'title': 'Home', 'url': reverse('core:index')},
        {'title': 'Equipamentos', 'url': reverse('core:listar_equipamentos')},
        {'title': 'Equipamento - Detalhes', 'url': '.'},
    ]

    if request.method == 'POST':
        equipamento.nome = request.POST['nome']
        equipamento.categoria = request.POST['categoria']
        equipamento.status = request.POST['status']
        foto = request.FILES.get('foto')

        if equipamento.foto:
            if foto:
                equipamento.foto.delete()
                equipamento.foto = foto
        else:
            if foto:
                equipamento.foto = foto

        equipamento.save()

        # Renomear a foto para o ID do equipamento
        if foto:
            novo_nome_arquivo = f"{equipamento.id}.jpg"

            # Obter o caminho completo do arquivo antigo
            caminho_arquivo_antigo = equipamento.foto.path

            # Gerar o caminho completo do novo arquivo
            caminho_novo_arquivo_banco = 'static/img/equipments/' + novo_nome_arquivo

            caminho_novo_arquivo_fisico = '/workspace/coreui-django-boilerplate-v2/myproject/core/' + caminho_novo_arquivo_banco

            # Renomear o arquivo físico
            shutil.move(caminho_arquivo_antigo, caminho_novo_arquivo_fisico)

            equipamento.foto.name = caminho_novo_arquivo_banco

            equipamento.save()           
        

        return redirect('core:editar_equipamento', equipamento_id=equipamento_id)

    if equipamento.foto:
        foto_equipamento = equipamento.foto.url.replace('/myproject/core', '')
        context = {'equipamento': equipamento, 'foto_equipamento': foto_equipamento, 'breadcrumb': breadcrumb}
    else:
        context = {'equipamento': equipamento, 'breadcrumb': breadcrumb}

    return render(request, 'form_equipamento.html', context)

def criar_equipamento(request):
    breadcrumb = [
        {'title': 'Home', 'url': reverse('core:index')},
        {'title': 'Equipamentos', 'url': reverse('core:listar_equipamentos')},
        {'title': 'Criar Equipamento', 'url': '.'},
    ]

    if request.method == 'POST':
        nome = request.POST['nome']
        categoria = request.POST['categoria']
        status = request.POST['status']
        foto = request.FILES.get('foto')  # Obtém o arquivo de imagem enviado

        equipamento = Equipamento(nome=nome, status=status, foto=foto)
        equipamento.save()

        # Renomear a foto para o ID do equipamento
        if foto:
            novo_nome_arquivo = f"{equipamento.id}.jpg"

            # Obter o caminho completo do arquivo antigo
            caminho_arquivo_antigo = equipamento.foto.path

            # Gerar o caminho completo do novo arquivo
            caminho_novo_arquivo_banco = 'static/img/equipments/' + novo_nome_arquivo

            caminho_novo_arquivo_fisico = '/workspace/coreui-django-boilerplate-v2/myproject/core/' + caminho_novo_arquivo_banco

            # Renomear o arquivo físico
            shutil.move(caminho_arquivo_antigo, caminho_novo_arquivo_fisico)

            equipamento.foto.name = caminho_novo_arquivo_banco
            equipamento.save()

        return redirect('core:listar_equipamentos')

    context = {'breadcrumb': breadcrumb}
    return render(request, 'form_equipamento.html', context)    

def remover_foto_equipamento(request, equipamento_id):
    equipamento = get_object_or_404(Equipamento, pk=equipamento_id)

    # Verificar se o equipamento possui uma foto
    if equipamento.foto:
        # Apagar o arquivo da foto na origem
        arquivo_foto = '/workspace/coreui-django-boilerplate-v2/myproject/core' + equipamento.foto.name
        if os.path.exists(arquivo_foto):
            os.remove(arquivo_foto)

        # Remover a foto do banco de dados
        equipamento.foto.delete()

    # Redirecionar para a página de edição do equipamento
    return redirect('core:editar_equipamento', equipamento_id=equipamento.id)

def desabilitar_equipamento(request, equipamento_id):
    equipamento = get_object_or_404(Equipamento, id=equipamento_id)
    equipamento.status = "Excluído"
    equipamento.save()
    return redirect('core:editar_equipamento', equipamento_id=equipamento_id)

def listar_equipamentos(request):
    equipamentos = Equipamento.objects.all()
    query = request.GET.get('q')
    coluna = request.GET.get('coluna')
    page_title = 'Equipamentos'
    breadcrumb = [
        {'title': 'Home', 'url': reverse('core:index')},
        {'title': 'Equipamentos', 'url': '.'},
    ]

    if query:
        equipamentos = equipamentos.filter(nome__icontains=query)

    if coluna == 'nome':
        equipamentos = equipamentos.order_by('nome')
    elif coluna == 'categoria':
        equipamentos = equipamentos.order_by('categoria')
    elif coluna == 'status':
        equipamentos = equipamentos.order_by('status')

    total_equipamentos = len(equipamentos)

    # Configurar a quantidade de itens por página
    itens_por_pagina = 5
    paginator = Paginator(equipamentos, itens_por_pagina)

    # Obter o número da página atual
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'lista_equipamentos.html', {'equipamentos': page_obj, 'total_equipamentos': total_equipamentos, 'query': query, 'coluna': coluna, 'page_title': page_title, 'breadcrumb': breadcrumb})