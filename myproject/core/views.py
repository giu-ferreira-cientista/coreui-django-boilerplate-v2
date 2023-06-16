from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario, Emprestimo, Reserva, Equipamento
import os
import uuid

def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def _list(request):
    template_name = '_list.html'
    return render(request, template_name)


def _detail(request):
    template_name = '_detail.html'
    return render(request, template_name)


def _create(request):
    template_name = '_form.html'
    return render(request, template_name)

def dashboard(request):
    usuarios = Usuario.objects.all()
    emprestimos = Emprestimo.objects.all()
    reservas = Reserva.objects.all()
    equipamentos = Equipamento.objects.all()

    context = {
        'usuarios': usuarios,
        'emprestimos': emprestimos,
        'reservas': reservas,
        'equipamentos': equipamentos
    }

    return render(request, 'dashboard.html', context)


#def dashboard(request):
#    template_name = 'dashboard.html'
#    return render(request, template_name)


def breadcrumb(request):
    template_name = 'base/breadcrumb.html'
    return render(request, template_name)


def cards(request):
    template_name = 'base/cards.html'
    return render(request, template_name)


def carousel(request):
    template_name = 'base/carousel.html'
    return render(request, template_name)


def collapse(request):
    template_name = 'base/collapse.html'
    return render(request, template_name)


def forms(request):
    template_name = 'base/forms.html'
    return render(request, template_name)


def jumbotron(request):
    template_name = 'base/jumbotron.html'
    return render(request, template_name)


def list_group(request):
    template_name = 'base/list-group.html'
    return render(request, template_name)


def navs(request):
    template_name = 'base/navs.html'
    return render(request, template_name)


def pagination(request):
    template_name = 'base/pagination.html'
    return render(request, template_name)


def popovers(request):
    template_name = 'base/popovers.html'
    return render(request, template_name)


def progress(request):
    template_name = 'base/progress.html'
    return render(request, template_name)


def scrollspy(request):
    template_name = 'base/scrollspy.html'
    return render(request, template_name)


def switches(request):
    template_name = 'base/switches.html'
    return render(request, template_name)


def tables(request):
    template_name = 'base/tables.html'
    return render(request, template_name)


def tabs(request):
    template_name = 'base/tabs.html'
    return render(request, template_name)


def tooltips(request):
    template_name = 'base/tooltips.html'
    return render(request, template_name)


def brand_buttons(request):
    template_name = 'buttons/brand-buttons.html'
    return render(request, template_name)


def button_group(request):
    template_name = 'buttons/button-group.html'
    return render(request, template_name)


def buttons(request):
    template_name = 'buttons/buttons.html'
    return render(request, template_name)


def dropdowns(request):
    template_name = 'buttons/dropdowns.html'
    return render(request, template_name)


def charts(request):
    template_name = 'charts.html'
    return render(request, template_name)


def colors(request):
    template_name = 'colors.html'
    return render(request, template_name)


def coreui_icons(request):
    template_name = 'icons/coreui-icons.html'
    return render(request, template_name)


def flags(request):
    template_name = 'icons/flags.html'
    return render(request, template_name)


def font_awesome(request):
    template_name = 'icons/font-awesome.html'
    return render(request, template_name)


def simple_line_icons(request):
    template_name = 'icons/simple-line-icons.html'
    return render(request, template_name)


def alerts(request):
    template_name = 'notifications/alerts.html'
    return render(request, template_name)


def badge(request):
    template_name = 'notifications/badge.html'
    return render(request, template_name)


def modals(request):
    template_name = 'notifications/modals.html'
    return render(request, template_name)


def typography(request):
    template_name = 'typography.html'
    return render(request, template_name)


def widgets(request):
    template_name = 'widgets.html'
    return render(request, template_name)


def login(request):
    template_name = 'login.html'
    return render(request, template_name)


def register(request):
    template_name = 'register.html'
    return render(request, template_name)


def error404(request):
    template_name = '404.html'
    return render(request, template_name)


def error500(request):
    template_name = '500.html'
    return render(request, template_name)


def invoice(request):
    template_name = 'invoice.html'
    return render(request, template_name)

def editar_equipamento(request, equipamento_id):
    equipamento = get_object_or_404(Equipamento, pk=equipamento_id)

    if request.method == 'POST':
        equipamento.nome = request.POST['nome']
        equipamento.status = request.POST['status']
        foto = request.FILES.get('foto')  # Obtém o arquivo de imagem enviado

        if equipamento.foto:
            # Verifica se um novo arquivo de foto foi enviado
            if foto:
                # Remove a foto anterior
                equipamento.foto.delete()
                equipamento.foto = foto
        else:
            # Se não houver uma foto associada ao equipamento, associa o novo arquivo de foto
            # Verifica se um novo arquivo de foto foi enviado
            if foto:
                equipamento.foto = foto

        equipamento.save()
        return redirect('core:dashboard')

    # Obter a URL da foto e remover a parte indesejada
    if equipamento.foto:
        foto_equipamento = equipamento.foto.url.replace('/myproject/core', '')
        context = {'equipamento': equipamento, 'foto_equipamento': foto_equipamento}
    else:
        context = {'equipamento': equipamento}        

    return render(request, 'form_equipamento.html', context)


import shutil

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


        return redirect('core:dashboard')

    return render(request, 'form_equipamento.html')

def remover_foto(request, equipamento_id):
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
