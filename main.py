from classes.gerenciador.GerenciadorEstoque import GerenciadorEstoque
from classes.produto.Produto import Produto
from dados.funcoesDados import carregar_dados, salvar_dados


def main():
    gerenciador = GerenciadorEstoque()
    carregar_dados(gerenciador)

    while True:
        print("\n===== Gerenciador de Estoque =====")
        print("\nEscolha uma opção:")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Buscar produto")
        print("4. Mostrar estoque")
        print("5. Mostrar histórico")
        print("6. Mostrar estoque ordenado")
        print("7. Adicionar pedido de reposição")
        print("8. Processar pedido de reposição")
        print("10. Mostrar produtos com estoque baixo")
        print("11. Buscar produto por nome")
        print("12. Atualizar dados do produto")
        print("0. Sair")

        opcao = input("Opção: ")

        if opcao == '1':
            try:
                id = int(input("ID: "))
                nome = input("Nome: ")
                categoria = input("Categoria: ")
                marca = input("Marca: ")
                preco = float(input("Preço: "))
                quantidade = int(input("Quantidade: "))
                descricao = input("Descrição: ")
                local = input("Local: ")

                produto = Produto(id, nome, categoria, marca, preco, quantidade, descricao, local)
                gerenciador.adicionar_produto(produto)
                print("Produto adicionado com sucesso!")
            except ValueError:
                print("Entrada inválida. Verifique os valores inseridos.")
        elif opcao == '2':
            try:
                id = int(input("ID do produto a remover: "))
                quantidade = int(input("Quantidade a remover: "))
                gerenciador.remover_produto(id, quantidade)
            except ValueError:
                print("Entrada inválida. Verifique os valores inseridos.")
        elif opcao == '3':
            try:
                id = int(input("ID do produto a buscar: "))
                gerenciador.buscar_produto(id)
            except ValueError:
                print("Entrada inválida. Digite um número inteiro para o ID.")
        elif opcao == '4':
            gerenciador.mostrar_estoque()
        elif opcao == '5':
            gerenciador.mostrar_historico()
        elif opcao == '6':
            gerenciador.mostrar_estoque_ordenado()
        elif opcao == '7':
            try:
                id = int(input("ID do produto: "))
                quantidade = int(input("Quantidade: "))
                gerenciador.adicionar_pedido_reposicao(id, quantidade)
            except ValueError:
                print("Entrada inválida. Verifique os valores inseridos.")
        elif opcao == '8':
            gerenciador.processar_pedido_reposicao()
        elif opcao == '10':
            gerenciador.mostrar_produtos_estoque_baixo()
        elif opcao == '11':
            nome = input("Nome do produto: ")
            gerenciador.buscar_produto_por_nome(nome)
        elif opcao == '12':
            try:
                id = int(input("ID do produto a atualizar: "))
                gerenciador.atualizar_produto(id)
            except ValueError:
                print("Entrada inválida. Digite um número inteiro para o ID.")
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
