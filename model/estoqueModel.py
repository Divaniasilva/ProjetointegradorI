class Estoque():
    def __init__(self, nome, tipo, cor,estoque,unidade, id_produto,id=None, preco=None, dataCompra=None):
        self.id =id
        self.id_produto =id_produto
        self.nome =nome
        self.tipo =tipo
        self.cor =cor
        self.estoque =estoque
        self.unidade =unidade
        self.preco =preco
        self.dataCompra =dataCompra


    def atualizar(self, dados):
        try:
            self.id = dados["id"]
            self.id_produto=dados["id_produto"]
            self.nome = dados["nome"]
            self.tipo = dados["tipo"]
            self.cor = dados["cor"]
            self.estoque = dados["estoque"]
            self.unidade = dados["unidade"]
            self.preco = dados["preco"]
            self.id, self.nome, self.tipo,self.cor, self.estoque, self.unidade,self.preco, self.id_produto
            return self
        except Exception as e:
            print("Problema ao atualizar estoque")
            print(e)

    def __dict__(self):
        d = dict()
        try:
            d['id'] = self.id
        except:
            d['id'] = None
        d['nome'] = self.nome
        d['tipo']= self.tipo
        d['cor'] = self.cor
        d['estoque'] = self.estoque
        d["preco"] = self.preco
        d['unidade'] = self.unidade
        d['id_produto']=self.id_produto
        return d

    @staticmethod
    def cria(dados):
        try:
            nome = dados["nome"]
            tipo = dados["tipo"]
            cor = dados["cor"]
            estoque = dados["estoque"]
            unidade = dados["unidade"]
            preco = dados["preco"]
            id_produto=dados["id_produto"]
            return Estoque(nome=nome, tipo=tipo, cor=cor, estoque=estoque, unidade=unidade, id_produto=id_produto, preco=preco)
        except Exception as e:
            print("Problema ao criar novo estoque!")
            print(e)

    @staticmethod
    def cria_de_tupla(dados):
        try:
            id = dados[0]
            nome = dados[1]
            tipo = dados[2]
            cor = dados[3]
            estoque = dados[4]
            unidade = dados[5]
            id_produto = dados[6]
            return Estoque(nome=nome, tipo=tipo, cor=cor, estoque=estoque, unidade=unidade, id_produto=id_produto,id=id )
        except Exception as e:
            print("Problema ao criar novo estoque!")
            print(e)
            
    @staticmethod
    def cria_de_tupla_ultima_compra(dados):
        try:
            id = dados[0]
            nome = dados[1]
            tipo = dados[2]
            cor = dados[3]
            estoque = dados[4]
            unidade = dados[5]
            preco = dados[6]
            dataCompra =  dados[7]
            id_produto = dados[8]
            return Estoque(nome=nome, tipo=tipo, cor=cor, estoque=estoque, unidade=unidade, id_produto=id_produto, id=id, preco=preco, dataCompra=dataCompra)
        except Exception as e:
            print("Problema ao criar novo estoque!")
            print(e)
