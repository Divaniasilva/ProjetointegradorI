class Produtos():
    def __init__(self, nome, cor, unidade, id=None):
        self.id = id
        self.nome = nome
        self.cor = cor
        self.unidade = unidade


    def atualizar(self, dados):
        try:
            id = dados["id"]
            nome = dados["nome"]
            cor = dados["cor"]
            unidade = dados["unidade"]
            self.id, self.nome, self.cor, self.unidade
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
        d['cor'] = self.cor
        d['unidade'] = self.unidade
        return d

    @staticmethod
    def cria(dados):
        try:
            nome = dados["nome"]
            cor = dados["cor"]
            unidade = dados["unidade"]
            return Produtos(nome=nome, cor=cor, unidade=unidade)
        except Exception as e:
            print("Problema ao criar novo produto!")
            print(e)

    @staticmethod
    def cria_de_tupla(dados):
        try:
            id = dados[0]
            nome = dados[1]
            cor = dados[2]
            unidade = dados[3]
            return Produtos(id=id, nome=nome, cor=cor, unidade=unidade)
        except Exception as e:
            print("Problema ao criar novo produto!")
            print(e)
