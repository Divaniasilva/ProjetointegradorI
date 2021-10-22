from model.usuariosModel import Usuario
from infra.usuarios_dao import listar as listar_dao, novo as novo_dao, atualiza as atualiza_dao


def listar():
    return listar_dao()


def localiza(id_usuario):
    for usuario in listar_dao():
        if str(usuario.id) == str(id_usuario):
            return usuario
    return None

def novo(novo_usuario):
    p = Usuario.cria(novo_usuario)
    novo_dao(p.__dict__())
    return listar_dao()

def atualiza(novo_usuario):
    for p in listar_dao():
        #Nada de editar chaves primarias nem id
        if str(p.id)==str(novo_usuario['id']):
            atualiza_dao(novo_usuario)
            return p
    return None