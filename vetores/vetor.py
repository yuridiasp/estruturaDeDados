class Vetor:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__elementos = [None] * tamanho
        self.__posicao = 0

    def __str__(self):
        return ' '.join([str(i) for i in self.__elementos])

    def retornar_tamanho(self):
        return self.__tamanho

    def inserir_elemento_posicao(self, elemento, posicao):
        vetor_inicio = self.__elementos[:posicao] + [elemento]
        vetor_final = self.__elementos[posicao:]
        self.__elementos = vetor_inicio + vetor_final
        self.__posicao += 1
        self.__tamanho += 1

    def listar_elemento(self, posicao):
        return self.__elementos[posicao]

    def inserir_elemento_final(self, elemento):
        if self.__posicao >= self.retornar_tamanho():
            self.__elementos = self.__elementos + [None]
            self.__tamanho += 1
        self.__elementos[self.__posicao] = elemento
        self.__posicao += 1

    def contem(self, elemento):
        for i in range(self.__tamanho):
            e = self.listar_elemento(i)
            if elemento == e:
                return True
        return False

    def indice(self, elemento):
        for i in range(self.__tamanho):
            e = self.listar_elemento(i)
            if elemento == e:
                return i
        return -1

    def remover_elemento(self, elemento):
        posicao = self.indice(elemento)
        self.remover_posicao(posicao)

    def remover_posicao(self, posicao):
        vetor_inicio = self.__elementos[:posicao]
        vetor_final = self.__elementos[posicao + 1:]
        self.__elementos = vetor_inicio + vetor_final
        self.__posicao -= 1
        self.__tamanho -= 1
