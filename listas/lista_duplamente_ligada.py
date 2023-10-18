from .no_duplo import NoDuplo


class ListaDuplamenteLigada:

    def __init__(self):
        self.__tamanho = 0
        self.__primeiro_no = None
        self.__ultimo_no = None

    def __str__(self):
        no = self.primeiro_no
        elementos = '['
        while no:
            elementos = f"{elementos} {no.elemento}"
            no = no.proximo
        elementos = f"{elementos} ]"
        return elementos

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho

    @property
    def primeiro_no(self):
        return self.__primeiro_no

    @primeiro_no.setter
    def primeiro_no(self, primeiro_no):
        self.__primeiro_no = primeiro_no

    @property
    def ultimo_no(self):
        return self.__ultimo_no

    @ultimo_no.setter
    def ultimo_no(self, ultimo_no):
        self.__ultimo_no = ultimo_no

    def inserir(self, elemento):
        novo_no = NoDuplo(elemento)
        if self.esta_vazia():
            self.primeiro_no = novo_no
            self.ultimo_no = novo_no
        else:
            self.ultimo_no.proximo = novo_no
            novo_no.anterior = self.ultimo_no
            self.ultimo_no = novo_no
        self.tamanho += 1

    def inserir_indice(self, elemento, index):
        novo_no = NoDuplo(elemento)
        if index == 0:
            novo_no.proximo = self.primeiro_no
            self.primeiro_no.anterior = novo_no
            self.primeiro_no = novo_no
        elif index >= self.tamanho - 1:
            self.inserir(elemento)
        else:
            no_atual = self.no_indice(index)
            no_anterior = no_atual.anterior
            novo_no.anterior = no_anterior
            novo_no.proximo = no_atual
            no_atual.anterior = novo_no
            no_anterior.proximo = novo_no
        self.tamanho += 1

    def esta_vazia(self):
        return self.tamanho == 0

    def elemento_indice(self, index):
        no = self.no_indice(index)
        if no is not None:
            return no.elemento
        return None

    def no_indice(self, index):
        no = None
        for i in range(index + 1):
            if i == 0:
                no = self.primeiro_no
            else:
                no = no.proximo
        return no

    def indice(self, elemento):
        for i in range(self.tamanho):
            no = self.no_indice(i)
            if no.elemento == elemento:
                return i
        return -1

    def contem(self, elemento):
        if self.indice(elemento) == -1:
            return False
        return True

    def remover_elemento(self, elemento):
        index = self.indice(elemento)
        self.remover_indice(index)

    def remover_indice(self, index):
        tamanho = self.tamanho
        if index == 0:
            proximo_no = self.primeiro_no.proximo
            self.primeiro_no = None
            self.primeiro_no = proximo_no
        elif index >= tamanho - 1:
            penultimo_no = self.ultimo_no.anterior
            self.ultimo_no.anterior = None
            penultimo_no.proximo = None
            self.ultimo_no = penultimo_no
        else:
            no_remover = self.no_indice(index)
            no_anterior = no_remover.anterior
            no_anterior.proximo = no_remover.proximo
            no_remover.proximo = None
            no_remover.anterior = None
        self.tamanho -= 1
