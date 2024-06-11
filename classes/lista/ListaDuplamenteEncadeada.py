from .NodeLista import NodeLista

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def adicionar_movimentacao(self, produto, tipo_movimentacao, quantidade):
        novo_node = NodeLista(produto, tipo_movimentacao, quantidade)
        if self.inicio is None:
            self.inicio = novo_node
            self.fim = novo_node
        else:
            self.fim.proximo = novo_node
            novo_node.anterior = self.fim
            self.fim = novo_node

    def mostrar_historico(self):
        atual = self.inicio
        while atual is not None:
            print(f"Produto: {atual.produto.nome}, Tipo: {atual.tipo_movimentacao}, Quantidade: {atual.quantidade}")
            atual = atual.proximo
