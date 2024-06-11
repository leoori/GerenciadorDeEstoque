import tkinter as tk
from tkinter import ttk
from classes.gerenciador.GerenciadorEstoque import GerenciadorEstoque
from classes.produto.Produto import Produto
from dados.funcoesDados import carregar_dados, salvar_dados
from funcoes.quick_sort.quick_sort import quick_sort

class InterfaceGerenciadorEstoque:
    def __init__(self, master):
        self.master = master
        master.title("Gerenciador de Estoque")

        self.gerenciador = GerenciadorEstoque()
        carregar_dados(self.gerenciador)  # Carrega os dados ao iniciar

        self.criar_widgets()

    def criar_widgets(self):
        # Labels e Entries
        labels = ["ID:", "Nome:", "Categoria:", "Marca:", "Preço:", "Quantidade:", "Descrição:", "Local:"]
        for i, label_text in enumerate(labels):
            tk.Label(self.master, text=label_text).grid(row=i, column=0, sticky="w")
            setattr(self, f"{label_text.lower()[:-1]}_entry", tk.Entry(self.master))
            getattr(self, f"{label_text.lower()[:-1]}_entry").grid(row=i, column=1)

        # Botões
        botoes = [
            ("Adicionar", self.adicionar_produto),
            ("Remover", self.remover_produto),
            ("Buscar por ID", self.buscar_produto_por_id),
            ("Buscar por Nome", self.buscar_produto_por_nome),
            ("Mostrar Estoque", self.mostrar_estoque),
            ("Mostrar Histórico", self.mostrar_historico),
            ("Mostrar Ordenado", self.mostrar_estoque_ordenado),
            ("Adicionar Pedido", self.adicionar_pedido_reposicao),
            ("Processar Pedido", self.processar_pedido_reposicao),
            ("Estoque Baixo", self.mostrar_produtos_estoque_baixo),
            ("Atualizar Produto", self.atualizar_produto),
        ]

        for i, (texto, comando) in enumerate(botoes):
            tk.Button(self.master, text=texto, command=comando).grid(row=i + 8, column=0, columnspan=2, sticky="ew")

        # Mensagens
        self.mensagem_label = tk.Label(self.master, text="")
        self.mensagem_label.grid(row=20, column=0, columnspan=2)


    # ... (implementação dos métodos para cada operação, como adicionar_produto, remover_produto, etc.)
    def adicionar_produto(self):
        try:
            id = int(self.id_entry.get())
            nome = self.nome_entry.get()
            categoria = self.categoria_entry.get()
            marca = self.marca_entry.get()
            preco = float(self.preço_entry.get())
            quantidade = int(self.quantidade_entry.get())
            descricao = self.descrição_entry.get()
            local = self.local_entry.get()

            produto = Produto(id, nome, categoria, marca, preco, quantidade, descricao, local)
            self.gerenciador.adicionar_produto(produto)
            self.mensagem_label.config(text="Produto adicionado com sucesso!")
        except ValueError:
            self.mensagem_label.config(text="Entrada inválida. Verifique os valores inseridos.")

    def remover_produto(self):
        try:
            id = int(self.id_entry.get())
            quantidade = int(self.quantidade_entry.get())
            self.gerenciador.remover_produto(id, quantidade)
            self.mensagem_label.config(text="Produto removido com sucesso!")
        except ValueError:
            self.mensagem_label.config(text="Entrada inválida. Verifique os valores inseridos.")

    def buscar_produto_por_id(self):
        try:
            id = int(self.id_entry.get())
            node = self.gerenciador.arvore.buscar(id)
            if node is None:
                self.mensagem_label.config(text="Produto não encontrado.")
            else:
                self.mensagem_label.config(
                    text=f"Produto: {node.produto.nome}, Quantidade: {node.produto.quantidade}"
                )
        except ValueError:
            self.mensagem_label.config(text="Entrada inválida. Digite um número inteiro para o ID.")

    def buscar_produto_por_nome(self):
        nome = self.nome_entry.get()
        resultado = self.gerenciador.buscar_produto_por_nome(nome)
        if resultado is None:
            self.mensagem_label.config(text="Produto não encontrado.")

    def mostrar_estoque(self):
        estoque_text = ""
        for produto in self.gerenciador.arvore.percorrer_em_ordem():
            estoque_text += f"ID: {produto.id}, Nome: {produto.nome}, Quantidade: {produto.quantidade}\n"
        self.mensagem_label.config(text=estoque_text)

    def mostrar_historico(self):
        historico_text = ""
        atual = self.gerenciador.historico.inicio
        while atual is not None:
            historico_text += f"Produto: {atual.produto.nome}, Tipo: {atual.tipo_movimentacao}, Quantidade: {atual.quantidade}\n"
            atual = atual.proximo
        self.mensagem_label.config(text=historico_text)

    def mostrar_estoque_ordenado(self):
        estoque_text = ""
        produtos_ordenados = quick_sort(self.gerenciador.arvore.percorrer_em_ordem())
        for produto in produtos_ordenados:
            estoque_text += f"ID: {produto.id}, Nome: {produto.nome}, Quantidade: {produto.quantidade}\n"
        self.mensagem_label.config(text=estoque_text)

    def adicionar_pedido_reposicao(self):
        try:
            id_produto = int(self.id_entry.get())
            quantidade = int(self.quantidade_entry.get())
            self.gerenciador.adicionar_pedido_reposicao(id_produto, quantidade)
            self.mensagem_label.config(text="Pedido de reposição adicionado.")
        except ValueError:
            self.mensagem_label.config(text="Entrada inválida. Verifique os valores inseridos.")

    def processar_pedido_reposicao(self):
        self.gerenciador.processar_pedido_reposicao()
        self.mensagem_label.config(text="Pedido de reposição processado (se houver).")

    def mostrar_produtos_estoque_baixo(self):
        limite = 10  # Ou você pode obter o limite de um Entry
        estoque_baixo_text = ""
        for produto in self.gerenciador.arvore.percorrer_em_ordem():
            if produto.quantidade <= limite:
                estoque_baixo_text += f"ID: {produto.id}, Nome: {produto.nome}, Quantidade: {produto.quantidade}\n"
        if estoque_baixo_text:
            self.mensagem_label.config(text=estoque_baixo_text)
        else:
            self.mensagem_label.config(text="Não há produtos com estoque baixo.")

    def atualizar_produto(self):
        try:
            id = int(self.id_entry.get())
            self.gerenciador.atualizar_produto(id)
            self.mensagem_label.config(text="Produto atualizado com sucesso!")
        except ValueError:
            self.mensagem_label.config(text="Entrada inválida. Digite um número inteiro para o ID.")



    def salvar_dados(self):
        salvar_dados(self.gerenciador)
        self.mensagem_label.config(text="Dados salvos com sucesso!")



if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceGerenciadorEstoque(root)
    root.mainloop()
