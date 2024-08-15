import json
from Aula_CRUD.view.view import View
                
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
    
    ##### cliente opções ######
    @staticmethod 
    def cliente_listar():
        for cliente in View.cliente_listar():
            print(cliente)
    @staticmethod 
    def cliente_inserir():
        nome = input("Informe o nome do cliente: ")
        email = input("Informe o e-mail do cliente: ")
        fone = input("Informe o telefone do cliente: ")
        
        View.cliente_inserir(nome, email, fone)
    @staticmethod 
    def cliente_atualizar():
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser atualizado: "))
        
        nome = input("Informe o novo nome para o cliente: ")
        email = input("Informe o novo e-mail para o cliente: ")
        fone = input("Informe o novo fone para o cliente: ")
        View.cliente_atualizar(id, nome, email, fone)
    @staticmethod 
    def cliente_excluir():
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser excluído: "))
        View.cliente_excluir(id)
    
    #################produto opcoes##############
    @staticmethod 
    def produto_listar():
        for produtos in View.produto_listar():
            print(produtos)
    @staticmethod 
    def produto_inserir():
        descricao = input('Informe a descrição do produto: ')
        preco = float(input('Informe o preço do produto: '))
        estoque = int(input('Informe quantas unidades deste produto tem no estoque: '))
        idCategoria = int(input('Informe o identificador da categoria do produto: '))
        
        View.produto_inserir(descricao, preco, estoque, idCategoria)
    @staticmethod 
    def produto_atualizar():
        UI.produto_listar()
        id = int(input("Informe o id do produto a ser atualizado: "))
        
        descricao = input('Informe a nova descrição para o produto: ')
        preco = float(input('Informe o novo preço para o produto: '))
        estoque = int(input('Informe quantas unidades deste produto tem no estoque: '))
        idCategoria = int(input('Informe o novo identificador da categoria do produto: '))
        View.produto_atualizar(id, descricao, preco, estoque, idCategoria)
    @staticmethod 
    def produto_excluir():
        UI.produto_listar()
        id = int(input("Informe o id do produto a ser excluído: "))
        View.produto_excluir(id, "", "", "", "")
    
    #############categoria opcoes#################
    @staticmethod 
    def categoria_listar():
        for categoria in View.categoria_listar():
            print(categoria)
    @staticmethod 
    def categoria_inserir():
        descricao = input('Informe a descrição da categoria: ')
        
        View.categoria_inserir(descricao)
    @staticmethod 
    def categoria_atualizar():
        UI.categoria_listar()
        id = int(input("Informe o id da categoria a ser atualizada: "))
        
        descricao = input('Informe a nova descrição para a categoria: ')
        View.categoria_atualizar(id, descricao)
    @staticmethod 
    def categoria_excluir():
        UI.categoria_listar()
        id = int(input("Informe o id da categoria a ser excluído: "))
        View.categoria_excluir(id)

UI.main()