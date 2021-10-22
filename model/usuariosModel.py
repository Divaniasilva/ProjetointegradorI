class Usuario():
    
    def __init__(self, nome, telefone, email, documento, cep, logradouro, numero, bairro, cidade, estado, idCategoria, senha, id=None):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.documento = documento
        self.cep = cep
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.idCategoria = idCategoria
        self.senha = senha

    
    def atualizar(self, dados):
        try:
            id = dados["id"]
            nome = dados["nome"]
            telefone = dados["telefone"]
            email = dados["email"]
            documento = dados["documento"]
            cep = dados["cep"]
            logradouro = dados["logradouro"]
            numero = dados["numero"]
            bairro = dados["bairro"]
            cidade = dados["cidade"]
            estado = dados["estado"]
            idCategoria = dados["idCategoria"]
            senha = dados["senha"]
            self.id, self.nome, self.telefone, self.email, self.documento, self.cep, self.logradouro, self.numero,self.bairro, self.cidade, self.estado, self.idCategoria, self.senha = id, nome, telefone, email, documento, cep, logradouro, numero, bairro, cidade, estado, idCategoria, senha
            return self
        except Exception as e:
            print("Problema ao criar novo usuario!")
            print(e)

    def __dict__(self):
        d = dict()
        d['nome'] = self.nome
        d['telefone'] = self.telefone
        d['email'] = self.email
        d['documento'] = self.documento
        d['cep'] = self.cep
        d['logradouro'] = self.logradouro
        d['numero'] = self.numero
        d['bairro']= self.bairro
        d['cidade'] = self.cidade
        d['estado']=self.estado
        d['idCategoria'] = self.idCategoria
        d['senha'] = self.senha
        return d

    @staticmethod
    def cria(dados):
        try:
            nome = dados["nome"]
            telefone = dados["telefone"]
            email = dados["email"]
            documento = dados["documento"]
            cep = dados["cep"]
            logradouro = dados["logradouro"]
            numero = dados["numero"]
            bairro = dados["bairro"]
            cidade = dados["cidade"]
            estado = dados["estado"]
            idCategoria = dados["idCategoria"]
            senha = dados["senha"]
            return Usuario(nome=nome, telefone=telefone, email=email, documento=documento, cep=cep, logradouro=logradouro, numero=numero, bairro=bairro, cidade=cidade, estado=estado, idCategoria=idCategoria, senha=senha)
        except Exception as e:
            print("Problema ao criar novo usuario!")
            print(e)

    @staticmethod
    def cria_de_tupla(registro):
        try:
            id = registro[0]
            nome = registro[1]
            telefone = registro[2]
            email = registro[3]
            documento = registro[4]
            cep = registro[5]
            logradouro = registro[6]
            numero = registro[7]
            bairro = registro[8]
            cidade = registro[9]
            estado = registro[10]
            idCategoria = registro[11]
            senha = registro[12]
            return Usuario(id=id, nome=nome, telefone=telefone, email=email, documento=documento, cep=cep,logradouro=logradouro, numero=numero, bairro=bairro, cidade=cidade, estado=estado, idCategoria=idCategoria, senha=senha)
        except Exception as e:
            print("Problema ao criar novo usuario!")
            print(e)
