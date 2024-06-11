from classes.arvore.ArvoreBinariaBusca import ArvoreBinariaBusca
from classes.lista.ListaDuplamenteEncadeada import ListaDuplamenteEncadeada
from dados.funcoesDados import salvar_dados
from funcoes.quick_sort.quick_sort import quick_sort
from classes.fila.Fila import Fila

class GerenciadorEstoque:
    def __init__(self):
        self.arvore = ArvoreBinariaBusca()
        self.historico = ListaDuplamenteEncadeada()
        self.pedidos_reposicao = Fila()

    def adicionar_produto(self, produto):
        self.arvore.inserir(produto)
        self.historico.adicionar_movimentacao(produto, "entrada", produto.quantidade)
        salvar_dados(self)

    def remover_produto(self, id, quantidade):
        node = self.arvore.buscar(id)
        if node is None:
            print("Produto não encontrado.")
            return

        if node.produto.quantidade < quantidade:
            print("Quantidade insuficiente em estoque.")
            return

        node.produto.quantidade -= quantidade
        self.historico.adicionar_movimentacao(node.produto, "saida", quantidade)

        if node.produto.quantidade == 0:
            self.arvore.remover(id)
        
        salvar_dados(self)

    def buscar_produto(self, id):
        node = self.arvore.buscar(id)
        if node is None:
            print("Produto não encontrado.")
        else:
            print(f"Produto: {node.produto.nome}, Quantidade: {node.produto.quantidade}")

    def mostrar_estoque(self):
        produtos = self.arvore.percorrer_em_ordem()
        for produto in produtos:
            print(f"ID: {produto.id}, Nome: {produto.nome}, Quantidade: {produto.quantidade}")

    def mostrar_historico(self):
        self.historico.mostrar_historico()

    def mostrar_estoque_ordenado(self):
        produtos = self.arvore.percorrer_em_ordem()
        produtos_ordenados = quick_sort(produtos)
        for produto in produtos_ordenados:
            print(f"ID: {produto.id}, Nome: {produto.nome}, Quantidade: {produto.quantidade}")

    def adicionar_pedido_reposicao(self, id_produto, quantidade):
        produto = self.arvore.buscar(id_produto)
        if produto is None:
            print("Produto não encontrado.")
        else:
            self.pedidos_reposicao.enfileirar(produto, quantidade)
            print("Pedido de reposição adicionado.")

    def processar_pedido_reposicao(self):
        pedido = self.pedidos_reposicao.desenfileirar()
        if pedido is None:
            print("Não há pedidos de reposição.")
        else:
            node_arvore, quantidade = pedido
            produto = node_arvore.produto  # Acessa o objeto Produto dentro do NodeArvore
            produto.quantidade += quantidade
            print(f"Pedido de reposição processado: {produto.nome} ({quantidade})")

    def mostrar_produtos_estoque_baixo(self, limite=10):
        print("\nProdutos com estoque baixo:")
        for produto in self.arvore.percorrer_em_ordem():
            if produto.quantidade <= limite:
                print(f"ID: {produto.id}, Nome: {produto.nome}, Quantidade: {produto.quantidade}")

    def buscar_produto_por_nome(self, nome):
        for produto in self.arvore.percorrer_em_ordem():
            if produto.nome.lower() == nome.lower():  # Ignora maiúsculas/minúsculas
                print(f"ID: {produto.id}, Nome: {produto.nome}, Quantidade: {produto.quantidade}")
                return
        print("Produto não encontrado.")

    def atualizar_produto(self, id):
        node = self.arvore.buscar(id)
        if node is None:
            print("Produto não encontrado.")
            return

        produto = node.produto
        print("\nDados atuais do produto:")
        print(f"ID: {produto.id}")
        print(f"Nome: {produto.nome}")
        print(f"Categoria: {produto.categoria}")
        print(f"Marca: {produto.marca}")
        print(f"Preço: {produto.preco:.2f}")
        print(f"Quantidade: {produto.quantidade}")
        print(f"Descrição: {produto.descricao}")
        print(f"Local: {produto.local}")

        while True:
            print("\nQual atributo deseja atualizar?")
            print("1. Nome")
            print("2. Categoria")
            print("3. Marca")
            print("4. Preço")
            print("5. Quantidade")
            print("6. Descrição")
            print("7. Local")
            print("0. Voltar")

            opcao = input("Opção: ")

            if opcao == '1':
                novo_nome = input("Novo nome: ")
                produto.nome = novo_nome
            elif opcao == '2':
                nova_categoria = input("Nova categoria: ")
                produto.categoria = nova_categoria
            elif opcao == '3':
                nova_marca = input("Nova marca: ")
                produto.marca = nova_marca
            elif opcao == '4':
                try:
                    novo_preco = float(input("Novo preço: "))
                    produto.preco = novo_preco
                except ValueError:
                    print("Entrada inválida. Digite um número para o preço.")
            elif opcao == '5':
                try:
                    nova_quantidade = int(input("Nova quantidade: "))
                    diferenca = nova_quantidade - produto.quantidade
                    produto.quantidade = nova_quantidade
                    self.historico.adicionar_movimentacao(produto, "ajuste", diferenca)
                except ValueError:
                    print("Entrada inválida. Digite um número inteiro para a quantidade.")
            elif opcao == '6':
                nova_descricao = input("Nova descrição: ")
                produto.descricao = nova_descricao
            elif opcao == '7':
                novo_local = input("Novo local: ")
                produto.local = novo_local
            elif opcao == '0':
                break
            else:
                print("Opção inválida.")