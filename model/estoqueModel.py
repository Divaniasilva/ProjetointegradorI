class Estoque():
    def __init__(self, nome, tipo, cor,estoque,unidade, id_produto,id=None, valor=None, dataCompra=None):
        self.id =id
        self.id_produto =id_produto
        self.nome =nome
        self.tipo =tipo
        self.cor =cor
        self.estoque =estoque
        self.unidade =unidade
        self.valor =valor
        self.dataCompra =dataCompra


    def atualizar(self, dados):
        try:
            id = dados["id"]
            id_produto=dados["id_produto"]
            nome = dados["nome"]
            tipo = dados["tipo"]
            cor = dados["cor"]
            estoque = dados["estoque"]
            unidade = dados["unidade"]
            self.id, self.nome, self.tipo,self.cor,self.estoque, self.unidade, self.id_produto
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
            id_produto=dados["id_produto"]
            return Estoque(nome=nome, tipo=tipo, cor=cor, estoque=estoque, unidade=unidade, id_produto=id_produto)
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
            valor = dados[6]
            dataCompra =  dados[7]
            id_produto = dados[8]
            return Estoque(nome=nome, tipo=tipo, cor=cor, estoque=estoque, unidade=unidade, id_produto=id_produto, id=id, valor=valor, dataCompra=dataCompra)
        except Exception as e:
            print("Problema ao criar novo estoque!")
            print(e)
