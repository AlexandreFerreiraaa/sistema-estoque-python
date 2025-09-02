from produto import Produto
from estoque import Estoque

estoque = Estoque()

def menu():
    while True:
        print("\n--- Sistema de Estoque ---")
        print("1. Cadastrar Produto")
        print("2. Adicionar ao Estoque")
        print("3. Remover do Estoque")
        print("4. Ajustar Estoque")
        print("5. Listar Produtos")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            codigo = input("Código do produto: ")
            nome = input("Nome do produto: ")
            categoria = input("Categoria: ")
            quantidade = int(input("Quantidade em estoque: "))
            preco = float(input("Preço: "))
            descricao = input("Descrição: ")
            fornecedor = input("Fornecedor: ")

            produto = Produto(codigo, nome, categoria, quantidade, preco, descricao, fornecedor)
            estoque.cadastrar_produto(produto)

        elif opcao == '2':
            codigo = input("Código do produto: ")
            qtd = int(input("Quantidade a adicionar: "))
            estoque.adicionar_estoque(codigo, qtd)

        elif opcao == '3':
            codigo = input("Código do produto: ")
            qtd = int(input("Quantidade a remover: "))
            estoque.remover_estoque(codigo, qtd)

        elif opcao == '4':
            codigo = input("Código do produto: ")
            nova_qtd = int(input("Nova quantidade: "))
            estoque.ajustar_estoque(codigo, nova_qtd)

        elif opcao == '5':
            estoque.listar_produtos()

        elif opcao == '6':
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

menu()
