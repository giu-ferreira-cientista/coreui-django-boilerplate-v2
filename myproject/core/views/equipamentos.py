from django.shortcuts import render, get_object_or_404, redirect
from ..models import Usuario, Emprestimo, Reserva, Equipamento
import os
import uuid
import shutil

def listar_equipamentos(request):
    equipamentos = Equipamento.objects.all()

    context = {
        'equipamentos': equipamentos
    }

    return render(request, 'lista_equipamentos.html', context)


def editar_equipamento(request, equipamento_id):
    equipamento = get_object_or_404(Equipamento, pk=equipamento_id)

    if request.method == 'POST':
        equipamento.nome = request.POST['nome']
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
        return redirect('core:editar_equipamento', equipamento_id=equipamento_id)

    if equipamento.foto:
        foto_equipamento = equipamento.foto.url.replace('/myproject/core', '')
        context = {'equipamento': equipamento, 'foto_equipamento': foto_equipamento}
    else:
        context = {'equipamento': equipamento}        

    return render(request, 'form_equipamento.html', context)

def criar_equipamento(request):
    if request.method == 'POST':
        nome = request.POST['nome']
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
            caminho_novo_arquivo_banco = '/static/img/equipments/' + novo_nome_arquivo

            caminho_novo_arquivo_fisico = '/workspace/coreui-django-boilerplate-v2/myproject/core/' + caminho_novo_arquivo_banco

            # Renomear o arquivo físico
            shutil.move(caminho_arquivo_antigo, caminho_novo_arquivo_fisico)

            equipamento.foto.name = caminho_novo_arquivo_banco
            equipamento.save()


        return redirect('core:listar_equipamentos')

    return render(request, 'form_equipamento.html')
    

def remover_foto_equipamento(request, equipamento_id):
    equipamento = get_object_or_404(Equipamento, pk=equipamento_id)

    # Verificar se o equipamento possui uma foto
    if equipamento.foto:
        # Apagar o arquivo da foto na origem
        arquivo_foto = equipamento.foto.path
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

def pesquisar_equipamentos(request):
    # Obtém o texto de pesquisa do parâmetro GET 'q'
    query = request.GET.get('q')

    # Filtra os equipamentos com base na consulta de pesquisa
    equipamentos = Equipamento.objects.filter(nome__icontains=query)

    # Renderiza o template com os equipamentos filtrados
    return render(request, 'lista_equipamentos.html', {'equipamentos': equipamentos})    