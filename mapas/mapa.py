from listas.lista_duplamente_ligada import ListaDuplamenteLigada
from .associacao import Association


class Mapa:
    def __init__(self):
        self.__elementos = ListaDuplamenteLigada()
        self.__numero_categorias = 10

        for i in range(self.__numero_categorias):
            self.__elementos.inserir(ListaDuplamenteLigada())

    def __str__(self):
        return self.__elementos.__str__()

    def __gerar_numero_espalhamento(self, chave):
        return hash(chave) % self.__numero_categorias

    def adicionar(self, chave, valor):
        if self.contem(chave):
            self.remover(chave)
        numero_espalhamento = self.__gerar_numero_espalhamento(chave)
        categoria = self.__elementos.elemento_indice(numero_espalhamento)
        categoria.inserir(Association(chave, valor))

    def remover(self, chave):
        numero_espalhamento = self.__gerar_numero_espalhamento(chave)
        categoria = self.__elementos.elemento_indice(numero_espalhamento)
        for i in range(categoria.tamanho):
            associacao = categoria.elemento_indice(i)
            print(f"Teste: {associacao}")
            if associacao.chave == chave:
                categoria.remover_elemento(associacao)
                return True
        return False

    def contem(self, chave):
        numero_espalhamento = self.__gerar_numero_espalhamento(chave)
        categoria = self.__elementos.elemento_indice(numero_espalhamento)
        for i in range(categoria.tamanho):
            associacao = categoria.elemento_indice(i)
            if associacao.chave == chave:
                return True
        return False

    def recuperar(self, chave):
        numero_espalhamento = self.__gerar_numero_espalhamento(chave)
        categoria = self.__elementos.elemento_indice(numero_espalhamento)
        for i in range(categoria.tamanho):
            associacao = categoria.elemento_indice(i)
            if associacao.chave == chave:
                return associacao.valor
        return False
