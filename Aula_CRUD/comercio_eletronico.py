import datetime
import json

class Cliente:
    def __init__(self, id, nome, email, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
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
    def set_data(self, data):
        if data == datetime: self.__data = data
        else: raise ValueError
    def set_carrinho(self, carrinho):
        if carrinho == bool: self.__carrinho = carrinho
        else: raise ValueError
    def set_total(self, total):
        if total == float: self.__total = total
        else: raise ValueError
    def set_idCliente(self, idCliente):
        if idCliente == int and idCliente > 0: self.__idCliente = idCliente
        else: raise ValueError
    def __str__(self):
        return f"{self.__id} - {self.__data} - {self.__carrinho} - {self.__total} - {self.__idCliente}"
    
class VendaItem:
    def __init__(self, id, qtd, preco, idVenda, idProduto):
        self.set_id(id)
        self.set_qtd(qtd)
        self.set_preco(preco)
        self.set_idVenda(idVenda)
        self.set_idProduto(idProduto)
    def get_id(self):
        return self.__id
    def get_qtd(self):
        return self.__qtd
    def get_preco(self):
        return self.__preco
    def get_idVenda(self):
        return self.__idVenda
    def get_idProduto(self):
        return self.__idProduto
    def set_id(self, id):
        if id > 0 and id == int: self.__id = id
        else: raise ValueError
    def set_qtd(self, qtd):
        if qtd > 0 and qtd == int: self.__qtd = qtd
        else: raise ValueError
    def set_preco(self, preco):
        if preco > 0 and preco == float: self.__preco = preco
        else: raise ValueError
    def set_idVenda(self, idVenda):
        if idVenda > 0 and idVenda == int: self.__idVenda = idVenda
        else: raise ValueError
    def set_idProduto(self, idProduto):
        if idProduto > 0 and idProduto == int: self.__idProduto = idProduto
        else: raise ValueError
    def __str__(self):
        return f"{self.__id} - {self.__qtd} - {self.__preco} - {self.__idVenda} - {self.__idProduto}"

class Produto:
    def __init__(self, id, descricao, preco, estoque, idCategoria):
        self.set_id(id)
        self.set_descricao(descricao)
        self.get_preco(preco)
        self.set_estoque(estoque)
        self.set_idCategoria(idCategoria)
    def get_id(self):
        return self.__id
    def get_descricao(self):
        return self.__descricao
    def get_preco(self):
        return self.__preco
    def get_estoque(self):
        return self.__estoque
    def get_idCategoria(self):
        return self.__idCategoria
    def set_id(self, id):
        if id > 0 and id == int: self.__id = id
        else: raise ValueError
    def set_descricao(self, descricao):
        if descricao == str: self.__descricao = descricao
        else: raise ValueError
    def set_preco(self, preco):
        if preco > 0 and preco == float: self.__preco = preco
        else: raise ValueError
    def set_estoque(self, estoque):
        if estoque == int: self.__estoque = estoque
        else: raise ValueError
    def set_idCategoria(self, idCategoria):
        if idCategoria > 0 and idCategoria == int: self.__idCategoria = idCategoria
        else: raise ValueError
    def __str__(self):
        return f"{self.__id} - {self.__descricao} - {self.__preco} - {self.__estoque} - {self.__idCategoria}"

class Categoria:
    def __init__(self, id, descricao):
        self.set_id(id)
        self.set_descricao(descricao)
    def get_id(self):
        return self.__id
    def get_descricao(self):
        return self.__descricao
    def set_id(self, id):
        if id > 0 and id == int: self.__id = id
        else: raise ValueError
    def set_descricao(self, descricao):
        if descricao == str: self.__descricao = descricao
        else: raise ValueError
    def __str__(self):
        return f"{self.__id} - {self.__descricao}"
        
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
