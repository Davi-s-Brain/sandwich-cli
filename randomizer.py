# Escolhe um sanduíche automáticamente

import os
from random import choice, randint

listaPaes = ['3 Queijos', 'Parmesão E orégano', '9 grãos', 'Italiano Branco']
listaQueijos = ['Cheddar', 'Suíço', 'Queijo Mussarela Ralada']
listaVegetais = ['Azeitonas', 'Picles', 'Pepinos', 'Pimentão', 'Alface',
                 'Cebola Roxa', 'Tomate', 'Rúcula']
listaMolhos = ['Cebola Agridoce', 'Chipotle', 'Barbecue', 'Parmesão',
               'Maionese Temperada', 'Mostarda E Mel', 'Supreme']

# Escolher a quantidade que quer no molho, ou deixar padrão


def remove_ingredientes(remove_ingredients: str):
    todasAsLista = listaPaes + listaQueijos + listaVegetais + listaMolhos
    print(todasAsLista, '\n')
    itensRemover = ''

    if (remove_ingredients == 'S'):
        while remove_ingredients == 'S':
            itensRemover = str(input('Escolha 1 ingrediente para remover:'))
            contido = itensRemover in todasAsLista

            if contido:
                todasAsLista.remove(itensRemover)
            else:
                print("Este item não existe na lista")

            os.system("cls")
            os.system("clear")
            print(todasAsLista)
            remove_ingredients = str(input('Deseja remover mais um? (S/N)'))

            if remove_ingredients == 'N':
                break

        return (os.system("cls"), os.system("clear"))

    else:
        return (os.system("cls"), os.system("clear"))


def escolhe_pao():
    pao = choice(listaPaes)
    return pao


def escolhe_queijo():
    queijo = choice(listaQueijos)
    return queijo


def escolhe_vegetais(quantidade_vegetais: int):
    vegetais = []

    if quantidade_vegetais != -1:
        for _ in range(quantidade_vegetais):
            escolhido = choice(listaVegetais)
            index_lista = listaVegetais.index(escolhido)
            vegetais.append(escolhido)
            listaVegetais.pop(index_lista)
    else:
        i = randint(2, 4)
        for _ in range(i):
            escolhido = choice(listaVegetais)
            index_lista = listaVegetais.index(escolhido)
            vegetais.append(escolhido)
            listaVegetais.pop(index_lista)

    return vegetais


def escolhe_molhos(quantidade_molhos):
    molho = []
    
    if quantidade_molhos != -1:
        for _ in range(quantidade_molhos):
            escolhido = choice(listaMolhos)
            index_lista = listaMolhos.index(escolhido)
            molho.append(escolhido)
            listaMolhos.pop(index_lista)
    else:
      i = randint(2, 3)
      for _ in range(i):
          escolhido = choice(listaMolhos)
          index_lista = listaMolhos.index(escolhido)
          molho.append(escolhido)
          listaMolhos.pop(index_lista)

    return molho


# def monta_sanduba():
#     escolhe_pao()
#     escolhe_queijo()
#     print('Recheio à vontade')
#     escolhe_vegetais()
#     escolhe_molhos()


# remove_ingredientes()
# monta_sanduba()
