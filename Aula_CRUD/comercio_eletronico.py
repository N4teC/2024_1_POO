import json

class Cliente:
    def __init__(self, id, nome, email, fone):
        self.get_id(id)
        self.get_nome(nome)
        self.get_email(email)
        self.get_fone(fone)
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_fone(self):
        return self.__fone
    def set_id(self, id):
        if id > 0 and id == int: self.__id = id
        else: raise ValueError
    def set_nome(self, nome):
        if nome == str: self.__nome = nome
        else: raise TypeError
    def set_email(self, email):
        if email == str: self.__email = email
        else: raise TypeError
    def set_fone(self, fone):
        if fone == int: self.__fone = fone
        else: raise TypeError
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

class Venda:
    def __init__(self, id, data, carrinho, total, idCliente):
        self.set_id(id)
        self.set_data(data)
        self.set_carrinho(carrinho)
        self.set_total(total)
        self.set_idCliente(idCliente)
    def get_id(self):
        return self.__id
    def get_data(self):
        return self.__data
    def get_carrinho(self):
        return self.__carrinho
    def get_total(self):
        return self.__total
    def get_idCliente(self):
        return self.__idCliente
    def set_id(self, id):
        if id > 0 and id == int: self.__id = id
        else: raise ValueError
    
    def __str__(self):
        return f"{self.__id} - {self.__data} - {self.__carrinho} - {self.__total} - {self.__idCliente}"
        
class VendaItem:
    def __init__(self, id, qtd, preco, idVenda, idProduto):
        self.id = id
        self.qtd = qtd
        self.preco = preco
        self.idVenda = idVenda
        self.idProduto = idProduto
    def __str__(self):
        return f"{self.id} - {self.qtd} - {self.preco} - {self.idVenda} - {self.idProduto}"

class Produto:
    def __init__(self, id, descricao, preco, estoque, idCategoria):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.idCategoria = idCategoria
    def __str__(self):
        return f"{self.id} - {self.descricao} - {self.preco} - {self.estoque} - {self.idCategoria}"

class Categoria:
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao
    def __str__(self):
        return f"{self.id} - {self.descricao}"
        
# Persistência: Modelo -> Arquivo Json    
class Clientes:
    objetos = []                # atributo da classe e não de uma instância da classe
    @classmethod
    def inserir(cls, obj):      # create - C
        cls.abrir()             # abre a lista de clientes do arquivo
        id = 0                  # cálculo do id do novo objeto
        for x in cls.objetos:
            if x.id > id: id = x.id
        id += 1    
        obj.id = id             # novo objeto recebe o id calculado
        cls.objetos.append(obj) # insere o objeto a lista
        cls.salvar()            # salva o arquivo
    @classmethod
    def listar(cls):            # read - R
        cls.abrir()
        return cls.objetos  
    @classmethod
    def listar_id(cls, id):           
        cls.abrir() 
        for x in cls.objetos:   # percorre a lista procurando o objeto com o id informado
            if x.id == id: return x
        return None      
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id) # x é o objeto que já está na lista com o mesmo id do objeto novo
        if x != None:
            x.nome = obj.nome
            x.email = obj.email
            x.fone = obj.fone
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id) # x é o objeto que já está na lista com o mesmo id do objeto novo
        if x != None: 
            cls.objetos.remove(x)
            cls.salvar()
    @classmethod
    def salvar(cls):    
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        with open("clientes.json", mode="r") as arquivo:
            texto_arquivo = json.load(arquivo)
            for obj in texto_arquivo:
                c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])
                cls.objetos.append(c)       
