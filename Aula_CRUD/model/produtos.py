import json

class Produto:
    def __init__(self, id:int, descricao:str, preco:float, estoque:int, idCategoria:int):
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
    
    def set_id(self, id:int):
        self.__id = id
    def set_descricao(self, descricao:str):
        self.__descricao = descricao
    def set_preco(self, preco:float):
        if preco > 0: self.__preco = preco
        else: raise ValueError
    def set_estoque(self, estoque:int):
        self.__estoque = estoque
    def set_idCategoria(self, idCategoria:int):
        self.__idCategoria = idCategoria
    def __str__(self):
        return f"{self.__id} - {self.__descricao} - {self.__preco} - {self.__estoque} - {self.__idCategoria}"

class Produtos:
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
            x.set_descricao(obj.get_descricao())
            x.set_preco(obj.get_preco())
            x.set_estoque(obj.get_estoque())
            x.set_idCategoria(obj.get_idCatgoria())
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.get_id()) # x é o objeto que já está na lista com o mesmo id do objeto novo
        if x != None: 
            cls.objetos.remove(x)
            cls.salvar()
    @classmethod
    def salvar(cls):    
        with open("./json/produtos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("./json/produtos.json", mode="r") as arquivo:
                texto_arquivo = json.load(arquivo)
                for obj in texto_arquivo:
                    p = Produto(obj["id"], obj["descricao"], obj["preco"], obj["estoque"], obj["idCategoria"])
                    cls.objetos.append(p)
        except FileNotFoundError:
            pass
                
