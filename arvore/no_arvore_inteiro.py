from arvore.no_arvore import NoArvore


class NoArvoreInteiro (NoArvore):
    def __init__(self):
        super().__init__()

    def peso(self):
        return self.valor
