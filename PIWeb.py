from flask import Flask
from API_usuarios import usuarios_app
import sqlite3

# inicializacao do bd SQLITE3
#con = sqlite3.connect('organic_shop')

#cur = con.cursor()

#FAZER VINCULO DE CHAVE ESTRANGEIRA DEPOIS COM TABELA DE IDCATEGORIAS

#tabela USUARIOS
#cur.execute("create table if not exists usuarios (id integer primary key autoincrement, nome varchar(100), telefone varchar(14), email varchar(100), documento varchar(20), cep varchar(10), logradouro varchar(200), numero varchar(10), bairro varchar(200), cidade varchar(100), estado varchar(60), idCategoria int, senha varchar(20) )")
#con.commit()

#cur.execute("create table if not exists produtos (id integer primary key autoincrement, id_fornecedor int, nome varchar(100), descricao varchar(400), quantidade integer, preco integer, status varchar(20))")
#con.commit()

#cur.execute("create table if not exists carrinho (id integer primary key autoincrement, id_usuario int, id_produto, quantidade, preco, valor_total,status varchar(40), data_criacao date deafult sysdate, ultima_atualizacao date default sysdate)")
#con.commit()

#cur.execute("create table if not exists venda (id integer primary key autoincrement, id_usuario int, qtd_itens int, total_venda floar, data_venda date)")
#con.commit()

app = Flask(__name__)
app.register_blueprint(usuarios_app)


if __name__ == '__main__':
    # subprocess.Popen("analise_banco_dados.py", shell=True)
    app.run(host='localhost', port=5000, debug=True)
    # app.run(host='localhost', port=5000, debug=True)
