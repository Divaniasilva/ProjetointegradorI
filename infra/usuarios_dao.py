import sqlite3
from model.usuariosModel import Usuario

def listar():
    usuarios = []
    con = sqlite3.connect('organic_shop')
    cur = con.cursor()    
    cur.execute("select id, nome, telefone, email, documento, cep, logradouro, numero, bairro, cidade, estado, idCategoria, senha from usuarios")
    
    usuarios = [Usuario.cria_de_tupla(linha) \
        for linha in cur.fetchall()]
    con.close()
    return usuarios

def novo(usuario_dicionario):
    con = sqlite3.connect('organic_shop')
    cur = con.cursor()    

    cur.execute("PRAGMA foreign_keys = ON;")
    con.commit()

    cur.execute("insert into usuarios (nome, telefone, email, documento, cep, logradouro, numero, bairro, cidade, estado, idCategoria, senha) values(:nome, :telefone, :email, :documento, :cep, :logradouro, :numero, :bairro, :cidade, :estado, :idCategoria, :senha)", usuario_dicionario)
    con.commit()
    con.close()

def atualiza(usuario_dicionario):
    con = sqlite3.connect('organic_shop')
    cur = con.cursor()   
    cur.execute("PRAGMA foreign_keys = ON;")
    con.commit()
    cur.execute("update usuarios set nome = :nome, telefone = :telefone, email = :email, cep = :cep, logradouro=:logradouro, numero = :numero, bairro=bairro, cidade=:cidade, estado=:estado, idCategoria = :idCategoria, senha = :senha where id = :id", usuario_dicionario)
    con.commit()
    con.close()
