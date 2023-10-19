from arvore.no_arvore import NoArvore


class NoArvoreInteiro (NoArvore):
    def __init__(self, valor):
        super().__init__(valor)

    def peso(self):
        return self.valor
