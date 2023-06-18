from django.urls import include, path
from myproject.core import views as v


app_name = 'core'


url_coreui = [
    path('dashboard/', v.dashboard, name='dashboard'),
    path('breadcrumb/', v.breadcrumb, name='breadcrumb'),
    path('cards/', v.cards, name='cards'),
    path('carousel/', v.carousel, name='carousel'),
    path('collapse/', v.collapse, name='collapse'),
    path('forms/', v.forms, name='forms'),
    path('jumbotron/', v.jumbotron, name='jumbotron'),
    path('list_group/', v.list_group, name='list_group'),
    path('navs/', v.navs, name='navs'),
    path('pagination/', v.pagination, name='pagination'),
    path('popovers/', v.popovers, name='popovers'),
    path('progress/', v.progress, name='progress'),
    path('scrollspy/', v.scrollspy, name='scrollspy'),
    path('switches/', v.switches, name='switches'),
    path('tables/', v.tables, name='tables'),
    path('tabs/', v.tabs, name='tabs'),
    path('tooltips/', v.tooltips, name='tooltips'),
    path('brand_buttons/', v.brand_buttons, name='brand_buttons'),
    path('button_group/', v.button_group, name='button_group'),
    path('buttons/', v.buttons, name='buttons'),
    path('dropdowns/', v.dropdowns, name='dropdowns'),
    path('charts/', v.charts, name='charts'),
    path('colors/', v.colors, name='colors'),
    path('coreui_icons/', v.coreui_icons, name='coreui_icons'),
    path('flags/', v.flags, name='flags'),
    path('font_awesome/', v.font_awesome, name='font_awesome'),
    path('simple_line_icons/', v.simple_line_icons, name='simple_line_icons'),
    path('login/', v.login, name='login'),
    path('alerts/', v.alerts, name='alerts'),
    path('badge/', v.badge, name='badge'),
    path('modals/', v.modals, name='modals'),
    path('register/', v.register, name='register'),
    path('typography/', v.typography, name='typography'),
    path('widgets/', v.widgets, name='widgets'),
    path('404/', v.error404, name='error404'),
    path('500/', v.error500, name='error500'),
    path('invoice/', v.invoice, name='invoice'),
    path('equipamentos/<int:equipamento_id>/editar/', v.editar_equipamento, name='editar_equipamento'),
    path('equipamentos/criar/', v.criar_equipamento, name='criar_equipamento'),
    path('equipamentos/<int:equipamento_id>/remover_foto/', v.remover_foto, name='remover_foto'),
    path('equipamentos/<int:equipamento_id>/desabilitar/', v.desabilitar_equipamento, name='desabilitar_equipamento'),
    path('equipamentos/pesquisar/', v.pesquisar_equipamentos, name='pesquisar_equipamentos'),
]


urlpatterns = [
    path('', v.index, name='index'),
    path('list/', v._list, name='list'),
    path('detail/', v._detail, name='detail'),
    path('add/', v._create, name='create'),
    path('coreui/', include(url_coreui)),
    
]
