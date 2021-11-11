from model.produtosModel import Produtos
from infra.produtos_dao import listar as listar_dao, novo as novo_dao, atualiza as atualiza_dao

def listar():
    return listar_dao()

def localiza(id_produto):
    for produtos in listar_dao():
        if str(produtos.id) == str(id_produto):
            return produtos
    return None

def novo(novo_produto):
    p = Produtos.cria(novo_produto)
    novo_dao(p.__dict__())
    return listar_dao()

def atualiza(novo_produto):
    for p in listar_dao():
        #Nada de editar chaves primarias nem id
        if str(p.id)==str(novo_produto['id']):
            atualiza_dao(novo_produto)
            return p
    return None