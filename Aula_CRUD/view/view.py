from Aula_CRUD.model.clientes import Cliente
from Aula_CRUD.model.clientes import Clientes
from Aula_CRUD.model.produtos import Produto
from Aula_CRUD.model.produtos import Produtos
from Aula_CRUD.model.categorias import Categoria
from Aula_CRUD.model.categorias import Categorias

class View:
    ##########################clientes################################
    @staticmethod 
    def cliente_listar():
        return Clientes.listar()
    @staticmethod 
    def cliente_inserir(nome:str, email:str, fone:str):
        a = Cliente(0, nome, email, fone)
        Clientes.inserir(a)
    @staticmethod 
    def cliente_atualizar(id:int, nome:str, email:str, fone:str):
        a = Cliente(id, nome, email, fone)
        Clientes.atualizar(a)
    @staticmethod 
    def cliente_excluir(id:int):
        a = Cliente(id, "", "", "")
        Clientes.excluir(a)
    ###########################produtos##############################
    @staticmethod 
    def produto_listar():
        return Produtos.listar()
    @staticmethod 
    def produto_inserir(descricao:str, preco:float, estoque:int, idCategoria:int):
        a = Produto(0, descricao, preco, estoque, idCategoria)
        Produtos.inserir(a)
    @staticmethod 
    def produto_atualizar(id:int, descricao:str, preco:float, estoque:int, idCategoria:int):
        a = Produto(id, descricao, preco, estoque, idCategoria)
        Produtos.atualizar(a)
    @staticmethod 
    def produto_excluir(id:int):
        a = Produto(id, "", "", "", "")
        Produtos.excluir(a)
    ##########################categoria opcoes########################
    @staticmethod 
    def categoria_listar():
        return Categorias.listar()
    @staticmethod 
    def categoria_inserir(descricao:str):
        a = Categoria(0, descricao)
        Categorias.inserir(a)
    @staticmethod 
    def categoria_atualizar(id:int, descricao:str):
        a = Categoria(id, descricao)
        Categorias.atualizar(a)
    @staticmethod 
    def categoria_excluir(id:int):
        a = Categoria(id, "")
        Categorias.excluir(a)