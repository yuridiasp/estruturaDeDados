from mapas import mapa
from conjuntos import conjunto
from filas import fila
from pilhas import pilha
from listas import lista_duplamente_ligada
from listas import lista_ligada
from listas import desafio_13_14
from vetores import vetor

# vetores_inteiros = array("b",[1, 2, 3])
# print(vetores_inteiros)
# vetores_inteiros.insert(3, 4)
# print(vetores_inteiros)
# print(vetores_inteiros.index(2))

print(30 * "-", "[ Menu ]", 30 * "-")
print("1. Vetores")
print("2. Listas Ligadas")
print("3. Desafio 13 Listas Ligadas")
print("4. Desafio 14 Listas Ligadas")
print("5. Listas Duplamente Ligadas")
print("6. Pilhas")
print("7. Filas")
print("8. Conjuntos")
print("9. Mapas")
print("10. Árvores")

menu = int(input("Digite opção desejada: "))

if menu == 1:
    vetor_teste = vetor.Vetor(3)
    # vetor_teste.inserir_elemento_posicao(1, 0)
    vetor_teste.inserir_elemento_final(1)
    vetor_teste.inserir_elemento_final(2)
    vetor_teste.inserir_elemento_final(3)
    vetor_teste.inserir_elemento_final(4)
    vetor_teste.inserir_elemento_final(5)
    vetor_teste.inserir_elemento_posicao(1, 2)
    print(vetor_teste)
if menu == 2:
    lista_teste = lista_ligada.ListaLigada()
    lista_teste.inserir(1)
    lista_teste.inserir(2)
    lista_teste.inserir(3)
    lista_teste.inserir(4)
    lista_teste.inserir(5)
    print(lista_teste)
    lista_teste.remover_indice(2)
    print(lista_teste)
if menu == 3:
    lista_desafio = desafio_13_14.ListaLigadaDesafio()
    for i in range(1, 6):
        lista_desafio.inserir(i)
    print(lista_desafio)
    lista_desafio.remover_elemento(1)
    print(lista_desafio)
if menu == 4:
    lista_desafio = desafio_13_14.ListaLigadaDesafio()
    for i in range(1, 6):
        lista_desafio.inserir(i)
    print(lista_desafio)
    lista_desafio.remove_n_elemento_do_fim(2)
    print(lista_desafio)
if menu == 5:
    lista_dupla_teste = lista_duplamente_ligada.ListaDuplamenteLigada()
    for i in range(1, 6):
        lista_dupla_teste.inserir(i)
    print(lista_dupla_teste)
    lista_dupla_teste.inserir_indice(6, 2)
    print(lista_dupla_teste)
    lista_dupla_teste.remover_elemento(3)
    print(lista_dupla_teste)
if menu == 6:
    pilha_teste = pilha.Pilha()
    for i in range(1, 6):
        pilha_teste.empilhar(i)
    print(pilha_teste)
    print(pilha_teste.desempilhar())
if menu == 7:
    fila_teste = fila.Fila()
    for i in range(1, 6):
        fila_teste.enfileirar(i)
    print(fila_teste)
    print(fila_teste.desenfileirar())
if menu == 8:
    conjunto_teste = conjunto.Conjunto()
    for i in range(1, 6):
        conjunto_teste.inserir(i)
    conjunto_teste.inserir("Python")
    print(conjunto_teste)
if menu == 9:
    mapa_teste = mapa.Mapa()
    mapa_teste.adicionar("par", 2)
    print(mapa_teste)
    mapa_teste.adicionar("impar", 1)
    print(mapa_teste)
    mapa_teste.adicionar("impar", 3)
    print(mapa_teste)
if menu == 10:
    pass
else:
    print("Opção Inválida")
