from .NodeFila import NodeFila

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enfileirar(self, produto, quantidade):
        novo_node = NodeFila(produto, quantidade)
        if self.fim is None:
            self.inicio = novo_node
            self.fim = novo_node
        else:
            self.fim.proximo = novo_node
            self.fim = novo_node

    def desenfileirar(self):
        if self.inicio is None:
            return None
        else:
            produto = self.inicio.produto
            quantidade = self.inicio.quantidade
            self.inicio = self.inicio.proximo
            if self.inicio is None:
                self.fim = None
            return produto, quantidade
