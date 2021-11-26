from flask import Flask, render_template, request, Blueprint

produtos_app = Blueprint('produtos_app', __name__, template_folder='templates')

from controller.produtosController import listar as service_listar, \
    localiza as service_localiza, \
    novo as service_novo, \
    atualiza as service_atualiza



@produtos_app.route("/produtos_lista")
def lista_produto():
    listados = list()
    produtos = service_listar()
    for produto in produtos:
       listados.append(produto)
    return render_template("lista_produtos.html", produtos=listados)

@produtos_app.route("/produto")
def validar_login():
    return render_template("cadastrar_produtos.html", mensagem = f"", editavel=None)
# @produtos_app.route("/produtos_lista")
# def form_prod():
#     return render_template("cadastrar_produtos.html", editavel="")

@produtos_app.route("/produtos", methods = ["POST"])
def cadastrar_produtos():
    novo_produto = dict()
    novo_produto["nome"] = request.form["id_nome_produto"]
    novo_produto["cor"] = request.form["id_cor"]
    novo_produto["unidade"] = request.form["id_unidade"]
    # print(novo_produto)
    new_user = novo_produto["nome"]
    print(novo_produto)
    service_novo(novo_produto)
    return render_template("cadastrar_produtos.html", mensagem = "Produto "+f"{new_user}, cadastrado com sucesso", editavel=None)

@produtos_app.route("/produtos/<id_produto>")
def rendireciona_update(id_produto):
    localizado = service_localiza(id_produto)
    return render_template("cadastrar_produtos.html", editavel=localizado)

@produtos_app.route("/produtos/<id_prod>", methods = ["POST"])
def editar_usuarios(id_prod):
    #ATUALIZAR PARA PEGAR APENAS OS DADOS DO PERFIL DAQUELE USUARIO
    edita_produto = dict()
    edita_produto["id"] = id_prod
    edita_produto["nome"] = request.form["id_nome_produto"]
    edita_produto["cor"] = request.form["id_cor"]
    edita_produto["unidade"] = request.form["id_unidade"]
    new_user = edita_produto["nome"];
    print('foi 1')
    service_atualiza(edita_produto)
    return render_template("cadastrar_produtos.html", mensagem = f"{new_user}, produto base editado", editavel=None)


# def bubble_sort(lista):
#     #KM DE VANTAGEM
#      elementos = len(lista)-1
#      ordenado = False
#      while not ordenado:
#          ordenado = True
#          for i in range(elementos):
#              if lista[i].km > lista[i+1].km:
#                  lista[i], lista[i+1] = lista[i+1],lista[i]
#                  ordenado = False     
#      return lista