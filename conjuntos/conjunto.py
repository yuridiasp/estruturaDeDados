from tabelas.tabela_espalhamento import TabelaEspalhamento


class Conjunto:
    def __init__(self):
        self.__elementos = TabelaEspalhamento()

    def __str__(self):
        return self.__elementos.__str__()

    def esta_vazia(self):
        return self.__elementos.tamanho == 0

    def inserir(self, elemento):
        return self.__elementos.inserir(elemento)

    # def inserir_indice(self, elemento, index):
    #     if not self.contem(elemento):
    #         self.__elementos.inserir_indice(elemento, index)
    #         return True
    #     return False

    def contem(self, elemento):
        return self.__elementos.contem(elemento)

    # def indice(self, elemento):
    #     return self.__elementos.indice(elemento)

    # def no_elemento(self, index):
    #     return self.__elementos.no_indice(index)

    # def tamanho(self):
    #     return self.__elementos.tamanho

    # def remover_index(self, index):
    #     self.__elementos.remover_indice(index)

    def remover_elemento(self, elemento):
        self.__elementos.remover_elemento(elemento)
