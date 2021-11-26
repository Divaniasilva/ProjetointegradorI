import mysql.connector as MySQL
from model.estoqueModel import Estoque


def listar():
    con = MySQL.connect(host="localhost",user="root",passwd="root",database="artes")
    cursor =con.cursor()
    cursor.execute("select c.id,pb.nome, c.tipo, pb.cor, format(sum(c.quantidade),2) 'Em Estoque', pb.unidade,pb.id from compras as c inner join produto_base as pb on c.id_produto = pb.id group by pb.id;")
    produtos = [Estoque.cria_de_tupla(linha) \
        for linha in cursor.fetchall()]
    con.close()
    return produtos 

def localiza_ultimas_compras():
    con=MySQL.connect(host="localhost",user="root",passwd="root",database="artes")
    cursor=con.cursor()  
    cursor.execute("select c.id, pb.nome, c.tipo, pb.cor, c.quantidade, pb.unidade, c.valor, DATE_FORMAT(c.data_compra, '%d/%m/%Y') as 'Ultima compra', c.id_produto from compras as c inner join produto_base as pb on c.id_produto = pb.id order by c.data_compra desc")
    produtos = [Estoque.cria_de_tupla_ultima_compra(linha) \
        for linha in cursor.fetchall()]
    con.close()
    return produtos 

def novo(estoque):
    con = MySQL.connect(host="localhost",user="root",passwd="root",database="artes")
    cursor =con.cursor()   
    cursor.execute("insert into produto_base(nome, cor, unidade) values('"+estoque['nome']+"','"+estoque["cor"]+"','"+estoque["unidade"]+"')")
    con.commit()
    con.close()


# def atualiza(estoque):
#     con = MySQL.connect(host="localhost",user="root",passwd="root",database="artes")
#     cursor =con.cursor()  
#     cursor.execute("update produto_base set nome = '"+produtos['nome']+"', cor = '"+produtos['cor']+"', unidade = '"+produtos['unidade']+"' where id='"+produtos['id']+"'")
#     con.commit()
#     con.close()
