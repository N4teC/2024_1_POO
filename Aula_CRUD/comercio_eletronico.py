import datetime
import json

class Cliente:
    def __init__(self, id:int, nome:str, email:str, fone:str):
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
    def set_id(self, id:int):
        self.__id = id
    def set_nome(self, nome:str):
        self.__nome = nome
    def set_email(self, email:str):
        self.__email = email
    def set_fone(self, fone:str):
        self.__fone = fone
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

class Venda:
    def __init__(self, id:int, data:str, carrinho:bool, total:float, idCliente:int):
        self.set_id(id)
        self.set_data(datetime.datetime.fromisoformat(data))
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
        self.__data = datetime.datetime.fromisoformat(data)
    def set_carrinho(self, carrinho:bool):
        self.__carrinho = carrinho
    def set_total(self, total:float):
        if total >= 0: self.__total = total
        else: raise ValueError
    def set_idCliente(self, idCliente:int):
        self.__idCliente = idCliente
    def __str__(self):
        return f"{self.__id} - {self.__data} - {self.__carrinho} - {self.__total} - {self.__idCliente}"
    
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

class Categoria:
    def __init__(self, id:int, descricao:str):
        self.set_id(id)
        self.set_descricao(descricao)
    def get_id(self):
        return self.__id
    def get_descricao(self):
        return self.__descricao
    def set_id(self, id:int):
        self.__id = id
    def set_descricao(self, descricao:str):
        self.__descricao = descricao
    def __str__(self):
        return f"{self.__id} - {self.__descricao}"
        
# Persistência: Modelo -> Arquivo Json    
class Clientes:
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
            x.set_nome(obj.get_nome())
            x.set_email(obj.get_email())
            x.set_fone(obj.get_fone())
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.get_id()) # x é o objeto que já está na lista com o mesmo id do objeto novo
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

# Persistência: Modelo -> Arquivo Json    
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
        with open("vendas.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        with open("vendas.json", mode="r") as arquivo:
            texto_arquivo = json.load(arquivo)
            for obj in texto_arquivo:
                v = Venda(obj["id"], obj["data"], obj["carrinho"], obj["total"], obj["idCliente"])
                cls.objetos.append(v)       

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
        with open("vendaitens.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        with open("vendaitens.json", mode="r") as arquivo:
            texto_arquivo = json.load(arquivo)
            for obj in texto_arquivo:
                v = VendaItem(obj["id"], obj["qtd"], obj["preco"], obj["idVenda"], obj["idProduto"])
                cls.objetos.append(v)
                
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
        with open("produtos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        with open("produtos.json", mode="r") as arquivo:
            texto_arquivo = json.load(arquivo)
            for obj in texto_arquivo:
                p = Produto(obj["id"], obj["descricao"], obj["preco"], obj["estoque"], obj["idCategoria"])
                cls.objetos.append(p)
                
class Categorias:
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
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.get_id()) # x é o objeto que já está na lista com o mesmo id do objeto novo
        if x != None: 
            cls.objetos.remove(x)
            cls.salvar()
    @classmethod
    def salvar(cls):    
        with open("categorias.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        with open("categorias.json", mode="r") as arquivo:
            texto_arquivo = json.load(arquivo)
            for obj in texto_arquivo:
                c = Categoria(obj["id"], obj["descricao"])
                cls.objetos.append(c)
                
class UI:
    @staticmethod
    def main():
        while True:
            i = UI.menu()
            
            if i[0] > 0 and i[0] < 5:
                #Opções válidas
                if i[0] == 1: #Clientes
                    if i[1] == 1: UI.cliente_listar()
                    elif i[1] == 2: UI.cliente_inserir()
                    elif i[1] == 3: UI.cliente_atualizar()
                    elif i[1] == 4: UI.cliente_excluir()
                elif i[0] == 2: #Produtos
                    if i[1] == 1: UI.produto_listar()
                    elif i[1] == 2: UI.produto_inserir()
                    elif i[1] == 3: UI.produto_atualizar()
                    elif i[1] == 4: UI.produto_excluir()
                elif i[0] == 3: #Categorias
                    if i[1] == 1: UI.categoria_listar()
                    elif i[1] == 2: UI.categoria_inserir()
                    elif i[1] == 3: UI.categoria_atualizar()
                    elif i[1] == 4: UI.categoria_excluir()
                elif i[0] == 4: #Sair
                    break
            else: print('Opção Inválida')
    @staticmethod 
    def menu():
        i = []
        print('1-Clientes | 2-Produtos | 3-Categorias | 4-Sair')
        i.append(int(input('Digite a opção que deseja interagir: ')))
        
        if i[0] >= 4 or i[0] <= 0:
            return i
        
        print('1 - Listar')
        print('2 - Adicionar')
        print('3 - Atualizar')
        print('4 - Excluir')
        print('Qualquer outra tecla - Voltar')
        i.append(int(input('Digite a opção que deseja interagir: ')))
        
        #print(i)
        return i
    @staticmethod 
    def produto_listar():
        for produtos in Produtos.listar():
            print(produtos)
    @staticmethod 
    def produto_inserir():
        descricao = input('Informe a descrição do produto: ')
        preco = float(input('Informe o preço do produto: '))
        estoque = int(input('Informe quantas unidades deste produto tem no estoque: '))
        idCategoria = int(input('Informe o identificador da categoria do produto: '))
        
        a = Produto(0, descricao, preco, estoque, idCategoria)
        Produtos.inserir(a)
    @staticmethod 
    def produto_atualizar():
        UI.produto_listar()
        id = int(input("Informe o id do produto a ser atualizado: "))
        
        descricao = input('Informe a nova descrição para o produto: ')
        preco = float(input('Informe o novo preço para o produto: '))
        estoque = int(input('Informe quantas unidades deste produto tem no estoque: '))
        idCategoria = int(input('Informe o novo identificador da categoria do produto: '))
        a = Produto(id, descricao, preco, estoque, idCategoria)
        Produtos.atualizar(a)
    @staticmethod 
    def produto_excluir():
        UI.produto_listar()
        id = int(input("Informe o id do produto a ser excluído: "))
        a = Produto(id, "", "", "", "")
        Produtos.excluir(a)
    @staticmethod 
    def categoria_listar():
        for categoria in Categorias.listar():
            print(categoria)
    @staticmethod 
    def categoria_inserir():
        descricao = input('Informe a descrição da categoria: ')
        
        a = Categoria(0, descricao)
        Categorias.inserir(a)
    @staticmethod 
    def categoria_atualizar():
        UI.categoria_listar()
        id = int(input("Informe o id da categoria a ser atualizada: "))
        
        descricao = input('Informe a nova descrição para a categoria: ')
        a = Categoria(id, descricao)
        Categorias.atualizar(a)
    @staticmethod 
    def categoria_excluir():
        UI.categoria_listar()
        id = int(input("Informe o id da categoria a ser excluído: "))
        a = Categoria(id, "")
        Categorias.excluir(a)
    @staticmethod 
    def cliente_listar():
        for cliente in Clientes.listar():
            print(cliente)
    @staticmethod 
    def cliente_inserir():
        nome = input("Informe o nome do cliente: ")
        email = input("Informe o e-mail do cliente: ")
        fone = input("Informe o telefone do cliente: ")
        
        a = Cliente(0, nome, email, fone)
        Clientes.inserir(a)
    @staticmethod 
    def cliente_atualizar():
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser atualizado: "))
        
        nome = input("Informe o novo nome para o cliente: ")
        email = input("Informe o novo e-mail para o cliente: ")
        fone = input("Informe o novo fone para o cliente: ")
        a = Cliente(id, nome, email, fone)
        Clientes.atualizar(a)
    @staticmethod 
    def cliente_excluir():
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser excluído: "))
        a = Cliente(id, "", "", "")
        Clientes.excluir(a)

UI.main()