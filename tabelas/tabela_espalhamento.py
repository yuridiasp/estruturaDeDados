from listas import lista_duplamente_ligada


# 0 (0, 50)
# 1 (51, 100)
# 2 (101, 150)
# 3 (151, 200)


class TabelaEspalhamento:
    def __init__(self):
        self.__elementos = lista_duplamente_ligada.ListaDuplamenteLigada()
        self.__numero_categorias = 10
        self.__tamanho = 0

        for i in range(self.__numero_categorias):
            self.__elementos.inserir(lista_duplamente_ligada.ListaDuplamenteLigada())

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho

    def __str__(self):
        return self.__elementos.__str__()

    def __gerar_numero_espalhamento(self, elemento):
        return hash(elemento) % self.__numero_categorias

    def inserir(self, elemento):
        if self.contem(elemento):
            return False
        numero_espalhamento = self.__gerar_numero_espalhamento(elemento)
        categoria = self.__elementos.elemento_indice(numero_espalhamento)
        categoria.inserir(elemento)
        self.tamanho += 1
        return True

    def contem(self, elemento):
        numero_espalhamento = self.__gerar_numero_espalhamento(elemento)
        categoria = self.__elementos.elemento_indice(numero_espalhamento)
        return categoria.contem(elemento)

    def remover_elemento(self, elemento):
        numero_espalhamento = self.__gerar_numero_espalhamento(elemento)
        categoria = self.__elementos.elemento_indice(numero_espalhamento)
        categoria.remover_elemento(elemento)
        self.tamanho -= 1

