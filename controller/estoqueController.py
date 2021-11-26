from model.estoqueModel import Estoque
from infra.estoque_dao import listar as listar_dao, novo as novo_dao, localiza_ultimas_compras

def listar():
    return listar_dao()

def localiza(id_estoque):
    for estoque in listar_dao():
        if str(estoque.id) == str(id_estoque):
            return estoque
    return None

def localiza_compras():
    estoque = localiza_ultimas_compras()
    return estoque
    
def novo(novo_estoque):
    p = Estoque.cria(novo_estoque)
    novo_dao(p.__dict__())
    return listar_dao()

# def atualiza(novo_estoque):
#     for p in listar_dao():
#         #Nada de editar chaves primarias nem id
#         if str(p.id)==str(novo_estoque['id']):
#             atualiza_dao(novo_estoque)
#             return p
#     return None