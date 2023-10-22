class Arvore:
    def __init__(self, raiz=None):
        self.__raiz = raiz

    @property
    def raiz(self):
        return self.__raiz

    @raiz.setter
    def raiz(self, raiz):
        self.__raiz = raiz

    def inserir_elemento(self, no):
        no.no_esquerdo = None
        no.no_direito = None
        if (self.raiz == None):
            self.raiz = no
        else:
            self.__inserir(self.raiz, no)

    def __inserir(self, referencia, no):
        if referencia.peso() < no.peso():
            if referencia.no_direito is None:
                referencia.no_direito = no
            else:
                self.__inserir(referencia.no_direito, no)
        else:
            if referencia.no_esquerdo is None:
                referencia.no_esquerdo = no
            else:
                self.__inserir(referencia.no_esquerdo, no)

    def buscar(self, no_busca):
        if self.raiz is None:
            return None
        else:
            return self.__buscar(self.raiz, no_busca)

    def __buscar(self, referencia, no_busca):
        if referencia.valor == no_busca.valor:
            return referencia
        elif referencia.peso() < no_busca.peso():
            if referencia.no_direito is None:
                raise ValueError("Elemento não encontrado")
            else:
                return self.__buscar(referencia.no_direito, no_busca)
        else:
            if referencia.no_esquerdo is None:
                raise ValueError("Elemento não encontrado")
            else:
                return self.__buscar(referencia.no_esquerdo, no_busca)

    def em_ordem(self):
        self.__em_ordem(self.raiz)

    def __em_ordem(self, referencia):
        if referencia.no_esquerdo != None:
            self.__em_ordem(referencia.no_esquerdo)
            print(referencia.valor.__str__())
            if referencia.no_direito != None:
                self.__em_ordem(referencia.no_direito)
        else:
            print(referencia.valor.__str__())
            if referencia.no_direito != None:
                self.__em_ordem(referencia.no_direito)

    def pre_ordem(self):
        self.__pre_ordem(self.raiz)

    def __pre_ordem(self, referencia):
        print(referencia.valor.__str__())
        if referencia.no_esquerdo != None:
            self.__pre_ordem(referencia.no_esquerdo)
            if referencia.no_direito != None:
                self.__pre_ordem(referencia.no_direito)
        else:
            if referencia.no_direito != None:
                self.__pre_ordem(referencia.no_direito)

    def pos_ordem(self):
        self.__pos_ordem(self.raiz)

    def __pos_ordem(self, referencia):
        if referencia.no_esquerdo != None:
            self.__pos_ordem(referencia.no_esquerdo)
            if referencia.no_direito != None:
                self.__pre_ordem(referencia.no_direito)
            print(referencia.valor.__str__())
        else:
            if referencia.no_direito != None:
                self.__pre_ordem(referencia.no_direito)
                print(referencia.valor.__str__())
            else:
                print(referencia.valor.__str__())

    def altura(self):
        return self.__altura(self.raiz)

    def __altura(self, referencia):
        if referencia is None:
            return -1
        altura_esquerda = self.__altura(referencia.no_esquerdo)
        altura_direita = self.__altura(referencia.no_direito)
        return (altura_esquerda + 1) if altura_esquerda > altura_direita else altura_direita + 1

    def __str__(self):
        return "[(X)]" if self.raiz is None else f"[({self.raiz.__str__()})]"
