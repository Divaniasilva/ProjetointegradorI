from flask import Flask, render_template, request, Blueprint, jsonify

estoque_app = Blueprint('estoque_app', __name__, template_folder='templates')

from controller.produtosController import listar as service_listar_produto
from controller.estoqueController import localiza_compras, listar as service_listar, \
    localiza as service_localiza, \
    novo as service_novo


@estoque_app.route("/estoque", methods = ["POST"])
def cadastra_estoque():
    estoque = dict()
    estoque["id_produto"] = request.form["produto"]
    for p in service_listar_produto():
        if str(p.id) == estoque["id_produto"]:
            estoque["nome"] = p.nome
            estoque["cor"] = p.cor
            estoque["unidade"] = p.unidade
            break
    
    estoque["tipo"]=request.form["id_tipo_produto"]
    estoque["estoque"]=request.form["id_qtd_produto"]
    estoque["preco"]=request.form["id_preco_produto"]
    localizado=service_novo(estoque)
    return render_template("home.html", mensagem="Estoque cadastrado com sucesso", estoque=localizado, editavel=None)


@estoque_app.route("/estoque")
def visualiza_estoque():
    localizado = service_listar_produto()
    return render_template("cadastrar_estoque.html", mensagem="", editavel=None,produtos=localizado)

@estoque_app.route("/estoque_lista")
def carrega_estoque():
    localizado=service_listar();
    return render_template("lista_estoque.html", mensagem="", editavel=None, estoque=localizado)

@estoque_app.route("/estoque/<id_estoque>", methods = ["GET","POST"])
def baixa_estoque(id_estoque):
    item = service_localiza(id_estoque)
    msg,estoque = realiza_baixa(item, request) 
    if(estoque != None):
        localizado=service_novo(estoque)
        site = "home.html"
    else:
        localizado=service_listar();
        site="lista_estoque.html"
    return render_template(site, mensagem=msg, editavel=None, estoque=localizado)

def realiza_baixa(item, estoque):
    if(float(estoque.form["id_baixa"].replace(",",".")) > float(item.estoque)):
        return "Quantidade insuficiente em estoque", None
    baixa=dict()
    baixa["nome"] = item.nome
    baixa["cor"] = item.cor
    baixa["unidade"] = item.unidade
    baixa["tipo"]=item.tipo
    baixa["estoque"]="-"+str(estoque.form["id_baixa"]).replace(",",".")
    baixa["id_produto"]=str(item.id_produto)
    baixa["preco"]="0"
    return "Baixa efetuada, estoque atualizado", baixa
    