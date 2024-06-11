from classes.produto.Produto import Produto

def carregar_dados(gerenciador, nome_arquivo_estoque="estoque.txt", nome_arquivo_historico="historico.txt"):
    carregar_estoque(gerenciador, nome_arquivo_estoque)
    carregar_historico(gerenciador, nome_arquivo_historico)

def carregar_estoque(gerenciador, nome_arquivo_estoque):
    try:
        with open(nome_arquivo_estoque, "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                if len(dados) == 8:  # Verifica se a linha tem todos os atributos
                    id, nome, categoria, marca, preco, quantidade, descricao, local = dados
                    produto = Produto(int(id), nome, categoria, marca, float(preco), int(quantidade), descricao, local)
                    gerenciador.adicionar_produto(produto)
    except FileNotFoundError:
        print(f"Arquivo de estoque '{nome_arquivo_estoque}' não encontrado. Iniciando com estoque vazio.")

def carregar_historico(gerenciador, nome_arquivo_historico):
    try:
        with open(nome_arquivo_historico, "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                if len(dados) == 4:  # ID, Nome, Tipo, Quantidade
                    id, nome, tipo_movimentacao, quantidade = dados
                    produto = gerenciador.arvore.buscar(int(id)).produto  # Busca o produto na árvore
                    gerenciador.historico.adicionar_movimentacao(produto, tipo_movimentacao, int(quantidade))
    except FileNotFoundError:
        print(f"Arquivo de histórico '{nome_arquivo_historico}' não encontrado.")

def salvar_dados(gerenciador, nome_arquivo_estoque="estoque.txt", nome_arquivo_historico="historico.txt"):
    salvar_estoque(gerenciador, nome_arquivo_estoque)
    salvar_historico(gerenciador, nome_arquivo_historico)

def salvar_estoque(gerenciador, nome_arquivo_estoque):
    with open(nome_arquivo_estoque, "w") as arquivo:
        for produto in gerenciador.arvore.percorrer_em_ordem():
            linha = f"{produto.id},{produto.nome},{produto.categoria},{produto.marca},{produto.preco:.2f},{produto.quantidade},{produto.descricao},{produto.local}\n"
            arquivo.write(linha)

def salvar_historico(gerenciador, nome_arquivo_historico):
    with open(nome_arquivo_historico, "w") as arquivo:
        atual = gerenciador.historico.inicio
        while atual is not None:
            linha = f"{atual.produto.id},{atual.produto.nome},{atual.tipo_movimentacao},{atual.quantidade}\n"
            arquivo.write(linha)
            atual = atual.proximo

