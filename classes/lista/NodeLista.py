class NodeLista:
    def __init__(self, produto, tipo_movimentacao, quantidade):
        self.produto = produto
        self.tipo_movimentacao = tipo_movimentacao  # "entrada" ou "saida"
        self.quantidade = quantidade
        self.anterior = None
        self.proximo = None