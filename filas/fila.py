from listas.lista_duplamente_ligada import ListaDuplamenteLigada


class Fila:
    def __init__(self):
        self._elementos = ListaDuplamenteLigada()

    def __str__(self):
        return self._elementos.__str__()

    def esta_vazia(self):
        return self._elementos.esta_vazia()

    def enfileirar(self, elemento):
        self._elementos.inserir(elemento)

    def desenfileirar(self):
        if self.esta_vazia():
            return None
        resultado = self._elementos.elemento_indice(0)
        self._elementos.remover_indice(0)
        return resultado
