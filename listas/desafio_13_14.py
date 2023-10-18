from .lista_ligada import ListaLigada


class ListaLigadaDesafio(ListaLigada):

    def __init__(self):
        super().__init__()

    def remover_elemento(self, index):
        tamanho = self.retornar_tamanho()
        if index == 1:
            no_remover = self.primeiro_no
            self.primeiro_no = no_remover.proximo
            no_remover = None
        elif index >= tamanho:
            penultimo_no = self.no_indice(index - 2)
            penultimo_no.proximo = None
            self.ultimo_no = penultimo_no
        else:
            no_remover = self.no_indice(index - 1)
            no_anterior = self.no_indice(index - 2)
            no_anterior.proximo = no_remover.proximo
            no_remover.proximo = None
        self.tamanho -= 1

    def remove_n_elemento_do_fim(self, number):
        self.remover_elemento(self.tamanho + 1 - number)
