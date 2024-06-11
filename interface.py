# interface.py

import tkinter as tk
from tkinter import ttk
from classes.gerenciador.GerenciadorEstoque import GerenciadorEstoque
from classes.produto.Produto import Produto
from dados.funcoesDados import carregar_dados, salvar_dados
from funcoes.quick_sort import quick_sort

class InterfaceGerenciadorEstoque:
    def __init__(self, master):
        self.master = master
        master.title("Gerenciador de Estoque")

        self.gerenciador = GerenciadorEstoque()
        carregar_dados(self.gerenciador)

        self.criar_widgets()

    def criar_widgets(self):
        # Botões
        botoes = [
            ("Adicionar", self.criar_widgets_adicionar_produto),
            ("Remover", self.criar_widgets_remover_produto),
            ("Buscar por ID", self.criar_widgets_buscar_produto_por_id),
            ("Buscar por Nome", self.criar_widgets_buscar_produto_por_nome),
            ("Mostrar Estoque", self.mostrar_estoque),
            ("Mostrar Histórico", self.mostrar_historico),
            ("Mostrar Ordenado", self.mostrar_estoque_ordenado),
            ("Adicionar Pedido", self.criar_widgets_adicionar_pedido_reposicao),
            ("Processar Pedido", self.processar_pedido_reposicao),
            ("Estoque Baixo", self.mostrar_produtos_estoque_baixo),
            ("Atualizar Produto", self.criar_widgets_atualizar_produto),
        ]

        for i, (texto, comando) in enumerate(botoes):
            tk.Button(self.master, text=texto, command=comando).grid(row=i, column=0, columnspan=2, sticky="ew")

        # Mensagens
        self.mensagem_label = tk.Label(self.master, text="")
        self.mensagem_label.grid(row=len(botoes), column=0, columnspan=2)

        # Botão Voltar (inicialmente desabilitado)
        self.botao_voltar = ttk.Button(self.master, text="Voltar", command=self.limpar_widgets, state=tk.DISABLED)
        self.botao_voltar.grid(row=len(botoes) + 1, column=0, columnspan=2, sticky="ew")

    def criar_widgets_adicionar_produto(self):
        self.limpar_widgets()  # Limpa widgets anteriores
        labels = ["ID:", "Nome:", "Categoria:", "Marca:", "Preço:", "Quantidade:", "Descrição:", "Local:"]
        for i, label_text in enumerate(labels):
            tk.Label(self.master, text=label_text).grid(row=i, column=0, sticky="w")
            setattr(self, f"{label_text.lower()[:-1]}_entry", tk.Entry(self.master))
            getattr(self, f"{label_text.lower()[:-1]}_entry").grid(row=i, column=1)

        tk.Button(self.master, text="Confirmar Adição", command=self.adicionar_produto).grid(
            row=len(labels), column=0, columnspan=2, sticky="ew"
        )
        
        

    def adicionar_produto(self):
        try:
            id = int(self.id_entry.get())
            nome = self.nome_entry.get()
            categoria = self.categoria_entry.get()
            marca = self.marca_entry.get()
            preco = float(self.preco_entry.get())
            quantidade = int(self.quantidade_entry.get())
            descricao = self.descricao_entry.get()
            local = self.local_entry.get()

            if not nome or preco <= 0 or quantidade <= 0:
                raise ValueError("Dados inválidos. Verifique nome, preço e quantidade.")

            produto = Produto(id, nome, categoria, marca, preco, quantidade, descricao, local)
            self.gerenciador.adicionar_produto(produto)
            self.mensagem_label.config(text="Produto adicionado com sucesso!", fg="green")
            self.limpar_widgets()  # Limpa os widgets após adicionar
        except ValueError as e:
            self.mensagem_label.config(text=f"Erro: {e}", fg="red")
        

    def criar_widgets_remover_produto(self):
        self.limpar_widgets()
        tk.Label(self.master, text="ID:").grid(row=0, column=0, sticky="w")
        self.id_entry = tk.Entry(self.master)
        self.id_entry.grid(row=0, column=1)
        tk.Label(self.master, text="Quantidade:").grid(row=1, column=0, sticky="w")
        self.quantidade_entry = tk.Entry(self.master)
        self.quantidade_entry.grid(row=1, column=1)
        tk.Button(self.master, text="Confirmar Remoção", command=self.remover_produto).grid(row=2, column=0, columnspan=2, sticky="ew")

    def criar_widgets_buscar_produto_por_id(self):
        self.limpar_widgets()
        tk.Label(self.master, text="ID:").grid(row=0, column=0, sticky="w")
        self.id_entry = tk.Entry(self.master)
        self.id_entry.grid(row=0, column=1)
        tk.Button(self.master, text="Buscar por ID", command=self.buscar_produto_por_id).grid(row=1, column=0, columnspan=2, sticky="ew")

    def criar_widgets_buscar_produto_por_nome(self):
        self.limpar_widgets()
        tk.Label(self.master, text="Nome:").grid(row=0, column=0, sticky="w")
        self.nome_entry = tk.Entry(self.master)
        self.nome_entry.grid(row=0, column=1)
        tk.Button(self.master, text="Buscar por Nome", command=self.buscar_produto_por_nome).grid(row=1, column=0, columnspan=2, sticky="ew")

    def criar_widgets_adicionar_pedido_reposicao(self):
        self.limpar_widgets()
        tk.Label(self.master, text="ID do Produto:").grid(row=0, column=0, sticky="w")
        self.id_entry = tk.Entry(self.master)
        self.id_entry.grid(row=0, column=1)
        tk.Label(self.master, text="Quantidade:").grid(row=1, column=0, sticky="w")
        self.quantidade_entry = tk.Entry(self.master)
        self.quantidade_entry.grid(row=1, column=1)
        tk.Button(self.master, text="Adicionar Pedido", command=self.adicionar_pedido_reposicao).grid(row=2, column=0, columnspan=2, sticky="ew")

    def criar_widgets_atualizar_produto(self):
        self.limpar_widgets()
        tk.Label(self.master, text="ID do Produto:").grid(row=0, column=0, sticky="w")
        self.id_entry = tk.Entry(self.master)
        self.id_entry.grid(row=0, column=1)
        tk.Button(self.master, text="Atualizar Produto", command=self.atualizar_produto).grid(row=1, column=0, columnspan=2, sticky="ew")


    def limpar_widgets(self):
        for widget in self.master.winfo_children():
            if widget not in (self.mensagem_label, self.botao_voltar):
                widget.destroy()
        self.botao_voltar.config(state=tk.DISABLED)  # Desabilita o botão Voltar

        # Recria o mensagem_label
        self.mensagem_label = tk.Label(self.master, text="")
        self.mensagem_label.grid(row=20, column=0, columnspan=2)

    def remover_produto(self):
        try:
            id = int(self.id_entry.get())
            quantidade = int(self.quantidade_entry.get())
            self.gerenciador.remover_produto(id, quantidade)
            self.mensagem_label.config(text="Produto removido com sucesso!", fg="green")
            self.limpar_widgets() 
        except ValueError:
            self.mensagem_label.config(text="Entrada inválida. Verifique os valores inseridos.", fg="red")

    def buscar_produto_por_id(self):
        try:
            id = int(self.id_entry.get())
            node = self.gerenciador.arvore.buscar(id)
            if node is None:
                self.mensagem_label.config(text="Produto não encontrado.", fg="red")
            else:
                self.mensagem_label.config(
                    text=f"Produto: {node.produto.nome}, Quantidade: {node.produto.quantidade}", fg="green"
                )
        except ValueError:
            self.mensagem_label.config(text="Entrada inválida. Digite um número inteiro para o ID.", fg="red")

    def buscar_produto_por_nome(self):
        nome = self.nome_entry.get()
        resultado = self.gerenciador.buscar_produto_por_nome(nome)
        self.mensagem_label.config(text="")  # Limpa a mensagem anterior
        if resultado is None:
            self.mensagem_label.config(text="Produto não encontrado.", fg="red")
        else:
            self.mensagem_label.config(
                text=f"ID: {resultado.id}, Nome: {resultado.nome}, Quantidade: {resultado.quantidade}", fg="green")

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

    def processar_pedido_reposicao(self):
        self.gerenciador.processar_pedido_reposicao()
        self.mostrar_estoque()
        self.mensagem_label.config(text="Pedido de reposição processado (se houver).")

    def mostrar_produtos_estoque_baixo(self):
        limite = 10
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

    def criar_botao_voltar(self):
        self.botao_voltar.config(state=tk.NORMAL)  # Habilita o botão Voltar




if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceGerenciadorEstoque(root)
    root.mainloop()
