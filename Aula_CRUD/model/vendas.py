import json
import datetime

class Venda:
    def __init__(self, id:int, data:str, carrinho:bool, total:float, idCliente:int):
        self.set_id(id)
        self.set_data(datetime.date.fromisoformat(data))
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
    def set_id(self, id:int):
        self.__id = id
    def set_data(self, data:str):
        self.__data = datetime.date.fromisoformat(data)
    def set_carrinho(self, carrinho:bool):
        self.__carrinho = carrinho
    def set_total(self, total:float):
        if total >= 0: self.__total = total
        else: raise ValueError
    def set_idCliente(self, idCliente:int):
        self.__idCliente = idCliente
    def __str__(self):
        return f"{self.__id} - {self.__data} - {self.__carrinho} - {self.__total} - {self.__idCliente}"
    
class Vendas:
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
            x.set_data(obj.get_data())
            x.set_carrinho(obj.get_carrinho())
            x.set_total(obj.get_total())
            x.set_idCliente(obj.get_idCliente())
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.get_id()) # x é o objeto que já está na lista com o mesmo id do objeto novo
        if x != None: 
            cls.objetos.remove(x)
            cls.salvar()
    @classmethod
    def salvar(cls):    
        with open("./json/vendas.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("./json/vendas.json", mode="r") as arquivo:
                texto_arquivo = json.load(arquivo)
                for obj in texto_arquivo:
                    v = Venda(obj["id"], obj["data"], obj["carrinho"], obj["total"], obj["idCliente"])
                    cls.objetos.append(v)
        except FileNotFoundError:
            pass