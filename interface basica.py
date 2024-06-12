import tkinter as tk
from tkinter import ttk
from classes.produto.Produto import Produto
from classes.arvore.ArvoreBinariaBusca import ArvoreBinariaBusca
from classes.lista.ListaDuplamenteEncadeada import ListaDuplamenteEncadeada
from funcoes.quick_sort.quick_sort import quick_sort
from classes.fila.Fila import Fila
from dados.funcoesDados import carregar_dados, salvar_dados
from classes.gerenciador.GerenciadorEstoque import GerenciadorEstoque

class GerenciadorEstoqueGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Estoque")

        self.gerenciador = GerenciadorEstoque()

        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        # Abas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Aba de Operações
        self.operacoes_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.operacoes_frame, text="Operações")

        # Adicionar Produto
        self.add_produto_frame = ttk.LabelFrame(self.operacoes_frame, text="Adicionar Produto")
        self.add_produto_frame.pack(padx=10, pady=10, fill=tk.BOTH)

        ttk.Label(self.add_produto_frame, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.id_entry = ttk.Entry(self.add_produto_frame)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.add_produto_frame, text="Nome:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.nome_entry = ttk.Entry(self.add_produto_frame)
        self.nome_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.add_produto_frame, text="Categoria:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.categoria_entry = ttk.Entry(self.add_produto_frame)
        self.categoria_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.add_produto_frame, text="Marca:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.marca_entry = ttk.Entry(self.add_produto_frame)
        self.marca_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(self.add_produto_frame, text="Preço:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.preco_entry = ttk.Entry(self.add_produto_frame)
        self.preco_entry.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(self.add_produto_frame, text="Quantidade:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.quantidade_entry = ttk.Entry(self.add_produto_frame)
        self.quantidade_entry.grid(row=5, column=1, padx=5, pady=5)

        ttk.Label(self.add_produto_frame, text="Descrição:").grid(row=6, column=0, padx=5, pady=5, sticky="e")
        self.descricao_entry = ttk.Entry(self.add_produto_frame)
        self.descricao_entry.grid(row=6, column=1, padx=5, pady=5)

        ttk.Label(self.add_produto_frame, text="Local:").grid(row=7, column=0, padx=5, pady=5, sticky="e")
        self.local_entry = ttk.Entry(self.add_produto_frame)
        self.local_entry.grid(row=7, column=1, padx=5, pady=5)

        self.add_produto_button = ttk.Button(self.add_produto_frame, text="Adicionar Produto", command=self.adicionar_produto)
        self.add_produto_button.grid(row=8, columnspan=2, pady=10)

        # Remover Produto
        self.remover_produto_frame = ttk.LabelFrame(self.operacoes_frame, text="Remover Produto")
        self.remover_produto_frame.pack(padx=10, pady=10, fill=tk.BOTH)

        ttk.Label(self.remover_produto_frame, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.remover_id_entry = ttk.Entry(self.remover_produto_frame)
        self.remover_id_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.remover_produto_frame, text="Quantidade:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.remover_quantidade_entry = ttk.Entry(self.remover_produto_frame)
        self.remover_quantidade_entry.grid(row=1, column=1, padx=5, pady=5)

        self.remover_produto_button = ttk.Button(self.remover_produto_frame, text="Remover Produto", command=self.remover_produto)
        self.remover_produto_button.grid(row=2, columnspan=2, pady=10)

        # Buscar Produto
        self.buscar_produto_frame = ttk.LabelFrame(self.operacoes_frame, text="Buscar Produto")
        self.buscar_produto_frame.pack(padx=10, pady=10, fill=tk.BOTH)

        ttk.Label(self.buscar_produto_frame, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.buscar_id_entry = ttk.Entry(self.buscar_produto_frame)
        self.buscar_id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.buscar_produto_button = ttk.Button(self.buscar_produto_frame, text="Buscar Produto", command=self.buscar_produto)
        self.buscar_produto_button.grid(row=1, columnspan=2, pady=10)

        # Exibir Estoque
        self.exibir_estoque_frame = ttk.LabelFrame(self.operacoes_frame, text="Exibir Estoque")
        self.exibir_estoque_frame.pack(padx=10, pady=10, fill=tk.BOTH)

        self.exibir_estoque_button = ttk.Button(self.exibir_estoque_frame, text="Exibir Estoque", command=self.exibir_estoque)
        self.exibir_estoque_button.pack(pady=10)

        # Exibir Histórico
        self.exibir_historico_frame = ttk.LabelFrame(self.operacoes_frame, text="Exibir Histórico")
        self.exibir_historico_frame.pack(padx=10, pady=10, fill=tk.BOTH)

        self.exibir_historico_button = ttk.Button(self.exibir_historico_frame, text="Exibir Histórico", command=self.exibir_historico)
        self.exibir_historico_button.pack(pady=10)

        # Mensagens
        self.messages_frame = ttk.LabelFrame(self.operacoes_frame, text="Mensagens")
        self.messages_frame.pack(padx=10, pady=10, fill=tk.BOTH)

        self.messages_text = tk.Text(self.messages_frame, wrap="word", height=5)
        self.messages_text.pack(expand=True, fill="both")

        # Aba de Pedidos de Reposição
        self.pedidos_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.pedidos_frame, text="Pedidos de Reposição")

        # Adicionar Pedido de Reposição
        self.add_pedido_frame = ttk.LabelFrame(self.pedidos_frame, text="Adicionar Pedido de Reposição")
        self.add_pedido_frame.pack(padx=10, pady=10, fill=tk.BOTH)

        ttk.Label(self.add_pedido_frame, text="ID do Produto:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.pedido_id_entry = ttk.Entry(self.add_pedido_frame)
        self.pedido_id_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.add_pedido_frame, text="Quantidade:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.pedido_quantidade_entry = ttk.Entry(self.add_pedido_frame)
        self.pedido_quantidade_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_pedido_button = ttk.Button(self.add_pedido_frame, text="Adicionar Pedido", command=self.adicionar_pedido)
        self.add_pedido_button.grid(row=2, columnspan=2, pady=10)

        # Processar Pedido de Reposição
        self.processar_pedido_frame = ttk.LabelFrame(self.pedidos_frame, text="Processar Pedido de Reposição")
        self.processar_pedido_frame.pack(padx=10, pady=10, fill=tk.BOTH)

        self.processar_pedido_button = ttk.Button(self.processar_pedido_frame, text="Processar Pedido", command=self.processar_pedido)
        self.processar_pedido_button.pack(pady=10)

        # Exibir Produtos com Estoque Baixo
        self.estoque_baixo_frame = ttk.LabelFrame(self.pedidos_frame, text="Produtos com Estoque Baixo")
        self.estoque_baixo_frame.pack(padx=10, pady=10, fill=tk.BOTH)

        self.exibir_estoque_baixo_button = ttk.Button(self.estoque_baixo_frame, text="Exibir Produtos", command=self.mostrar_produtos_estoque_baixo)
        self.exibir_estoque_baixo_button.pack(pady=10)

        # Mensagens
        self.messages_frame2 = ttk.LabelFrame(self.pedidos_frame, text="Mensagens")
        self.messages_frame2.pack(padx=10, pady=10, fill=tk.BOTH)

        self.messages_text2 = tk.Text(self.messages_frame2, wrap="word", height=5)
        self.messages_text2.pack(expand=True, fill="both")

        # Carregar e Salvar Dados
        self.load_save_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.load_save_frame, text="Carregar/Salvar Dados")

        self.load_data_button = ttk.Button(self.load_save_frame, text="Carregar Dados", command=self.load_data)
        self.load_data_button.pack(pady=10)

        self.save_data_button = ttk.Button(self.load_save_frame, text="Salvar Dados", command=self.save_data)
        self.save_data_button.pack(pady=10)

    def adicionar_produto(self):
        id = int(self.id_entry.get())
        nome = self.nome_entry.get()
        categoria = self.categoria_entry.get()
        marca = self.marca_entry.get()
        preco = float(self.preco_entry.get())
        quantidade = int(self.quantidade_entry.get())
        descricao = self.descricao_entry.get()
        local = self.local_entry.get()

        produto = Produto(id, nome, categoria, marca, preco, quantidade, descricao, local)
        self.gerenciador.adicionar_produto(produto)
        self.update_messages("Produto adicionado com sucesso!")

        # Limpar os campos após adicionar o produto
        self.clear_entry_fields([self.id_entry, self.nome_entry, self.categoria_entry, self.marca_entry, 
                                 self.preco_entry, self.quantidade_entry, self.descricao_entry, self.local_entry])

    def remover_produto(self):
        id = int(self.remover_id_entry.get())
        quantidade = int(self.remover_quantidade_entry.get())
        self.gerenciador.remover_produto(id, quantidade)
        self.update_messages("Produto removido com sucesso!")

        # Limpar os campos após remover o produto
        self.clear_entry_fields([self.remover_id_entry, self.remover_quantidade_entry])

    def buscar_produto(self):
        id = int(self.buscar_id_entry.get())
        self.gerenciador.buscar_produto(id)

        # Limpar os campos após buscar o produto
        self.clear_entry_fields([self.buscar_id_entry])

    def buscar_produto_por_nome(self):
        nome = self.buscar_nome_entry.get()
        self.gerenciador.buscar_produto_por_nome(nome)

        # Limpar os campos após buscar o produto
        self.clear_entry_fields([self.buscar_nome_entry])

    def exibir_estoque(self):
        self.gerenciador.mostrar_estoque()

    def exibir_historico(self):
        self.gerenciador.mostrar_historico()

    def adicionar_pedido(self):
        id_produto = int(self.pedido_id_entry.get())
        quantidade = int(self.pedido_quantidade_entry.get())
        self.gerenciador.adicionar_pedido_reposicao(id_produto, quantidade)
        self.update_messages2("Pedido de reposição adicionado com sucesso!")

        # Limpar os campos após adicionar o pedido de reposição
        self.clear_entry_fields([self.pedido_id_entry, self.pedido_quantidade_entry])

    def processar_pedido(self):
        self.gerenciador.processar_pedido_reposicao()
        self.update_messages2("Pedido de reposição processado com sucesso!")

    def mostrar_produtos_estoque_baixo(self):
        self.gerenciador.mostrar_produtos_estoque_baixo()

    def load_data(self):
        carregar_dados(self.gerenciador)
        self.update_messages("Dados carregados com sucesso!")

    def save_data(self):
        salvar_dados(self.gerenciador)
        self.update_messages("Dados salvos com sucesso!")

    def clear_entry_fields(self, entries):
        for entry in entries:
            entry.delete(0, tk.END)

    def update_messages(self, message):
        self.messages_text.insert(tk.END, message + "\n")
        self.messages_text.see(tk.END)

    def update_messages2(self, message):
        self.messages_text2.insert(tk.END, message + "\n")
        self.messages_text2.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = GerenciadorEstoqueGUI(root)
    root.mainloop()

