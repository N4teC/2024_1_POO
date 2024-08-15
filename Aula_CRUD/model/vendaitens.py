import json

class VendaItem:
    def __init__(self, id:int, qtd:int, preco:float, idVenda:int, idProduto:int):
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
    def set_id(self, id:int):
        self.__id = id
    def set_qtd(self, qtd:int):
        if qtd > 0: self.__qtd = qtd
        else: raise ValueError
    def set_preco(self, preco:float):
        if preco > 0: self.__preco = preco
        else: raise ValueError
    def set_idVenda(self, idVenda:int):
        self.__idVenda = idVenda
    def set_idProduto(self, idProduto:int):
        self.__idProduto = idProduto
    def __str__(self):
        return f"{self.__id} - {self.__qtd} - {self.__preco} - {self.__idVenda} - {self.__idProduto}"

class VendaItens:
    objetos = []                # atributo da classe e não de uma instância da classe
    @classmethod
    def inserir(cls, obj):      # create - C
        cls.abrir()             # abre a lista de objetos do arquivo
        id = 0                  # cálculo do id do novo objeto
        for x in cls.objetos:
            if x.get_id() > id: id = x.get_id()
        id += 1    
        obj.set_id(id)             # novo objeto recebe o id calculado
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
            if x.get_id() == id: return x
        return None      
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.get_id()) # x é o objeto que já está na lista com o mesmo id do objeto novo
        if x != None:
            x.set_qtd(obj.get_qtd())
            x.set_preco(obj.get_preco())
            x.set_idVenda(obj.get_idVenda())
            x.set_idProduto(obj.get_idProduto())
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.get_id()) # x é o objeto que já está na lista com o mesmo id do objeto novo
        if x != None: 
            cls.objetos.remove(x)
            cls.salvar()
    @classmethod
    def salvar(cls):    
        with open("./json/vendaitens.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        with open("./json/vendaitens.json", mode="r") as arquivo:
            texto_arquivo = json.load(arquivo)
            for obj in texto_arquivo:
                v = VendaItem(obj["id"], obj["qtd"], obj["preco"], obj["idVenda"], obj["idProduto"])
                cls.objetos.append(v)
                