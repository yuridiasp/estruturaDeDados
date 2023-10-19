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

    def __str__(self):
        return "[(X)]" if self.raiz is None else f"[({self.raiz.__str__()})]"
