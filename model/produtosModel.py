class Produtos():
    def __init__(self, id_fornecedor, nome, descricao, quantidade, preco, status, id=None):
        self.id = id
        self.id_fornecedor = id_fornecedor
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco = preco
        self.status = status
        self.km = 0


    def atualizar(self, dados):
        try:
            id = dados["id"]
            id_fornecedor = dados["id_fornecedor"]
            nome = dados["nome"]
            descricao = dados["descricao"]
            quantidade = dados["quantidade"]
            preco = dados["preco"]
            status = dados["status"]
            self.id, self.id_fornecedor, self.nome, self.descricao, self.quantidade, self.preco, self.status
            return self
        except Exception as e:
            print("Problema ao criar novo Produto")
            print(e)

    def __dict__(self):
        d = dict()
        try:
            d['id'] = self.id
        except:
            d['id'] = None
        d['nome'] = self.nome
        d['id_fornecedor'] = self.id_fornecedor
        d['descricao'] = self.descricao
        d['quantidade'] = self.quantidade
        d['preco'] = self.preco
        d['status'] = self.status
        return d

    @staticmethod
    def cria(dados):
        try:
            id_fornecedor = dados["id_fornecedor"]
            nome = dados["nome"]
            descricao = dados["descricao"]
            quantidade = dados["quantidade"]
            preco = dados["preco"]
            status = dados['status']
            return Produtos(id_fornecedor=id_fornecedor, nome=nome, descricao=descricao, quantidade=quantidade, preco=preco, status=status)
        except Exception as e:
            print("Problema ao criar novo produto!")
            print(e)

    @staticmethod
    def cria_de_tupla(dados):
        try:
            id = dados[0]
            id_fornecedor = dados[1]
            nome = dados[2]
            descricao = dados[3]
            quantidade = dados[4]
            preco = dados[5]
            status = dados[6]
            return Produtos(id=id, id_fornecedor=id_fornecedor, nome=nome, descricao=descricao, quantidade=quantidade, preco=preco, status=status)
        except Exception as e:
            print("Problema ao criar novo produto!")
            print(e)
