from .no import No


class ListaLigada:
    def __init__(self):
        self.__tamanho = 0
        self.__primeiro_no = None
        self.__ultimo_no = None

    @property
    def ultimo_no(self):
        return self.__ultimo_no

    @ultimo_no.setter
    def ultimo_no(self, ultimo_no):
        self.__ultimo_no = ultimo_no

    @property
    def primeiro_no(self):
        return self.__primeiro_no

    @primeiro_no.setter
    def primeiro_no(self, primeiro_no):
        self.__primeiro_no = primeiro_no

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho

    def inserir(self, elemento):
        novo_no = No(elemento)
        if self.esta_vazia():
            self.__primeiro_no = novo_no
            self.__ultimo_no = novo_no
        else:
            self.__ultimo_no.proximo = novo_no
            self.__ultimo_no = novo_no
        self.__tamanho += 1

    def inserir_indice(self, elemento, index):
        novo_no = No(elemento)
        if index == 0:
            novo_no.proximo = self.__primeiro_no
            self.__primeiro_no = novo_no
        elif index >= self.retornar_tamanho() - 1:
            self.inserir(elemento)
        else:
            atual = self.no_indice(index)
            anterior = self.no_indice(index - 1)
            novo_no.proximo = atual
            anterior.proximo = novo_no
        self.__tamanho += 1

    def esta_vazia(self):
        return self.__tamanho == 0

    def retornar_tamanho(self):
        return self.__tamanho

    def __str__(self):
        temp = self.__primeiro_no
        elementos = ''
        while temp:
            elementos = f'{elementos} {temp.elemento}'
            temp = temp.proximo
        return elementos

    def elemento_indice(self, index):
        no = self.no_indice(index)
        if no is not None:
            return no.elemento
        return None

    def no_indice(self, index):
        no = None
        for i in range(index + 1):
            if i == 0:
                no = self.__primeiro_no
            else:
                no = no.proximo
        return no

    def indice(self, elemento):
        for i in range(self.retornar_tamanho()):
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
        tamanho = self.retornar_tamanho()
        if index == 0:
            proximo_no = self.__primeiro_no.proximo
            self.__primeiro_no = None
            self.__primeiro_no = proximo_no
        elif index == tamanho - 1:
            penultimo_no = self.no_indice(tamanho - 2)
            penultimo_no.proximo = None
            self.__ultimo_no = penultimo_no
        else:
            no_remover = self.no_indice(index)
            no_anterior = self.no_indice(index - 1)
            no_anterior.proximo = no_remover.proximo
            no_remover.proximo = None
        self.__tamanho -= 1
