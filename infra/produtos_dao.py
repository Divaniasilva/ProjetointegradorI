import mysql.connector as MySQL
from model.produtosModel import Produtos


def listar():
    con = MySQL.connect(host="localhost",user="root",passwd="root",database="artes")
    cursor =con.cursor()
    cursor.execute("select id,nome,cor,unidade from produto_base")
    produtos = [Produtos.cria_de_tupla(linha) \
        for linha in cursor.fetchall()]
    #con.close()
    return produtos 


def novo(produtos):
    con = MySQL.connect(host="localhost",user="root",passwd="root",database="artes")
    cursor =con.cursor()   
    cursor.execute("insert into produto_base(nome, cor, unidade) values('"+produtos['nome']+"','"+produtos["cor"]+"','"+produtos["unidade"]+"')")
    con.commit()
    con.close()


def atualiza(produtos):
    con = MySQL.connect(host="localhost",user="root",passwd="root",database="artes")
    cursor =con.cursor()  
    cursor.execute("update produto_base set nome = '"+produtos['nome']+"', cor = '"+produtos['cor']+"', unidade = '"+produtos['unidade']+"' where id='"+produtos['id']+"'")
    con.commit()
    con.close()
