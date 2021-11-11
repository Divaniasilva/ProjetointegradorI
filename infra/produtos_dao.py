import sqlite3
from model.produtosModel import Produtos

def listar():
    produtos = []
    con = sqlite3.connect('organic_shop')
    cur = con.cursor()    
    cur.execute("select id, id_fornecedor, nome, descricao, quantidade, preco, status from produtos")
    
    produtos = [Produtos.cria_de_tupla(linha) \
        for linha in cur.fetchall()]
    con.close()
    return produtos


def novo(produtos):
    con = sqlite3.connect('organic_shop')
    cur = con.cursor()    

    cur.execute("PRAGMA foreign_keys = ON;")
    con.commit()

    cur.execute("insert into produtos (id_fornecedor, nome, descricao, preco, quantidade, status) values(:id_fornecedor, :nome, :descricao,:preco, :quantidade, :status)", produtos)
    con.commit()
    con.close()


def atualiza(produtos):
    con = sqlite3.connect('organic_shop')
    cur = con.cursor()   
    cur.execute("PRAGMA foreign_keys = ON;")
    con.commit()
    cur.execute("update produtos set nome = :nome, descricao = :descricao, quantidade = :quantidade, status = :status where id = :id", produtos)
    con.commit()
    con.close()
