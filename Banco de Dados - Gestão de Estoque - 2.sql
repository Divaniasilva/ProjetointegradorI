/*Banco de dados - Gestão de estoque*/

CREATE DATABASE GestãoEstoque;

USE GestãoEstoque;

/*Tabela de dados 'estoque_cadastro'*/
CREATE TABLE estoque_cadastro (
    id_cadastro INT,
    produto_nome VARCHAR(20),
    produto_tipo VARCHAR(20),
    produto_cor VARCHAR(10),
    unidade_medida VARCHAR(10),
    preço NUMERIC(10 , 2 ),
    data_compra DATE,
    PRIMARY KEY (id_cadastro) 
);

create table login(
id int primary key auto_increment,
codigo varchar(8) not null,
senha varchar(20) not null
);

insert into login(codigo, senha) values('4321','1234');

/*Dados para a tabela 'estoque_cadastro'*/
INSERT INTO estoque_cadastro (
id_cadastro, 
produto_nome, 
produto_tipo, 
produto_cor, 
unidade_medida, 
preço, 
data_compra) VALUES
 
(1,'Seda','Tecido','Branca','0',35,'2021-08-10'),
(2,'Seda','Tecido','Rosa','1M',35,'2021-08-10'),
(3,'Seda','Tecido','Azul','0',45,'2021-08-10'),
(4,'Lã','Tecido','Branca','0',35,'2021-08-10'),
(5,'Zíper','Tecido','Amarelo','1M',15,'2021-08-10'),
(6,'Botão','Material','Preto','1UN',10,'2021-08-10'),
(7,'Manta R1','Material','Branca','1M',45,'2021-08-10'),
(8,'Manta R2','Material','Branca','1M',45,'2021-08-10'),
(9,'Linha de costura','Material','Azul','1M',10,'2021-08-10'),
(10,'Linha de costura','Material','Branca','1M',10,'2021-08-10'),
(11,'Linha de costura','Material','Vermelho','1M',10,'2021-08-10'),
(12,'Agulha','Material','Padrão','1UN',11,'2021-08-10'),
(13,'Cursores','Material','Padrão','1UN',45,'2021-08-10');


/*Dados para a tabela 'estoque_disponível*/
CREATE TABLE estoque_disponível (
    id_cadastro INT PRIMARY KEY,
	unidade_medida VARCHAR(10),
    FOREIGN KEY (id_cadastro) REFERENCES estoque_cadastro (id_cadastro) ON DELETE CASCADE
);

INSERT INTO estoque_disponível (id_cadastro, unidade_medida);
SELECT id_cadastro, unidade_medida 
FROM estoque_cadastro
WHERE unidade_medida>0





