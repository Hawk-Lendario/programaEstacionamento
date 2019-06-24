from django.urls import path
from .views import (
    home,
    lista_pessoas,
    lista_veiculos,
    lista_movrotativos,
    lista_mensalistas,
    lista_mov_mensalistas,
    pessoa_novo,
    veiculo_novo,
    movrotativos_novo,
    mensalista_novo,
    movmensalista_novo,
    pessoa_update,
    veiculo_update,
    movrot_update,
    mensalista_update,
    movmensalista_update,
    pessoa_delete,
    veiculo_delete,
    movrot_delete,
    mensalista_delete,
    movmensalista_delete,
)


urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas', lista_pessoas, name='core_lista_pessoas'),
    path('pessoa_novo', pessoa_novo, name='core_pessoa_novo'),
    path('pessoa-update/<int:id>', pessoa_update, name='core_pessoa_update'),
    #<int:id> é um atributo, no casa o atributo é id
    path('pessoa-delete/<int:id>', pessoa_delete, name='core_pessoa_delete'),

    path('veiculos', lista_veiculos, name='core_lista_veiculos'),
    path('veiculo_novo', veiculo_novo, name='core_veiculo_novo'),
    path('veiculo-update/<int:id>', veiculo_update, name='core_veiculo_update'),
    path('veiculo-delete/<int:id>', veiculo_delete, name='core_veiculo_delete'),

    path('mov-rot', lista_movrotativos,
         name='core_lista_movrotativos'),
    path('mov-rot-novo', movrotativos_novo, name='core_movrotativos_novo'),
    path('mov-rot-update/<int:id>', movrot_update,
         name='core_movrot_update'),
    path('mov-rot-delete/<int:id>', movrot_delete, name='core_movrot_delete'),

    path('mensalistas', lista_mensalistas,
         name='core_lista_mensalistas'),
    path('mensalista_novo', mensalista_novo, name='core_mensalista_novo'),
    path('mensalista-update/<int:id>', mensalista_update, name='core_mensalista_update'),
    path('mensalista-delete/<int:id>', mensalista_delete, name='core_mensalista_delete'),

    path('mov-mensal', lista_mov_mensalistas,
         name='core_lista_mov_mensalistas'),
    path('mov_mensal_novo', movmensalista_novo, name='core_movmensalistas_novo'),
    path('mov-mensal-update/<int:id>', movmensalista_update,
         name='core_movmensalista_update'),
    path('movmensalista-delete/<int:id>', movmensalista_delete, name='core_movmensalista_delete'),



]

