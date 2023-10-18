from listas.lista_duplamente_ligada import ListaDuplamenteLigada


class Pilha:
    def __init__(self):
        self.__elementos = ListaDuplamenteLigada()

    def __str__(self):
        return self.__elementos.__str__()

    def esta_vazia(self):
        return self.__elementos.esta_vazia()

    def empilhar(self, elemento):
        self.__elementos.inserir(elemento)

    def desempilhar(self):
        if self.esta_vazia():
            return None
        resultado = self.__elementos.elemento_indice(self.__elementos.tamanho - 1)

        self.__elementos.remover_indice(self.__elementos.tamanho - 1)
        return resultado
