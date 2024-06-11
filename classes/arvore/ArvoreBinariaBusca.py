from .NodeArvore import NodeArvore

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, produto):
        if self.raiz is None:
            self.raiz = NodeArvore(produto)
        else:
            self._inserir_recursivo(produto, self.raiz)

    def _inserir_recursivo(self, produto, node):
        if produto.id < node.produto.id:
            if node.esquerda is None:
                node.esquerda = NodeArvore(produto)  # Cria um novo objeto NodeArvore
            else:
                self._inserir_recursivo(produto, node.esquerda)
        else:
            if node.direita is None:
                node.direita = NodeArvore(produto)  # Cria um novo objeto NodeArvore
            else:
                self._inserir_recursivo(produto, node.direita)

    def buscar(self, id):
        return self._buscar_recursivo(id, self.raiz)

    def _buscar_recursivo(self, id, node):  # Alterado o parâmetro para 'node'
        if node is None or node.produto.id == id:
            return node
        elif id < node.produto.id:
            return self._buscar_recursivo(id, node.esquerda)
        else:
            return self._buscar_recursivo(id, node.direita)

    def percorrer_em_ordem(self):
        produtos = []
        self._percorrer_em_ordem_recursivo(self.raiz, produtos)
        return produtos

    def _percorrer_em_ordem_recursivo(self, node, produtos):  # Alterado o parâmetro para 'node'
        if node is not None:
            self._percorrer_em_ordem_recursivo(node.esquerda, produtos)
            produtos.append(node.produto)  # Corrigido para 'node'
            self._percorrer_em_ordem_recursivo(node.direita, produtos)  # Corrigido para 'node'

    def remover(self, id):
        self.raiz = self._remover_recursivo(id, self.raiz)

    def _remover_recursivo(self, id, node):
        if node is None:
            return node

        if id < node.produto.id:
            node.esquerda = self._remover_recursivo(id, node.esquerda)
        elif id > node.produto.id:
            node.direita = self._remover_recursivo(id, node.direita)
        else:
            # Nó encontrado, vamos removê-lo
            if node.esquerda is None:
                return node.direita
            elif node.direita is None:
                return node.esquerda
            else:
                # Nó com dois filhos: substituir pelo sucessor em ordem
                sucessor = self._encontrar_minimo(node.direita)
                node.produto = sucessor.produto
                node.direita = self._remover_recursivo(sucessor.produto.id, node.direita)
        return node

    def _encontrar_minimo(self, node):
        while node.esquerda is not None:
            node = node.esquerda
        return node