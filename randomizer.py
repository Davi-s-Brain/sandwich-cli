# Escolhe um sanduíche automáticamente

from random import choice, randint

listaPaes = ['3 Queijos', 'Parmesão E orégano', '9 grãos', 'Italiano Branco']
listaQueijos = ['Cheddar', 'Suíço', 'Queijo Mussarela Ralada']
listaVegetais = ['Azeitonas', 'Picles', 'Pepinos', 'Pimentão', 'Alface',
                 'Cebola Roxa', 'Tomate', 'Rúcula']
listaMolhos = ['Cebola Agridoce', 'Chipotle', 'Barbecue', 'Parmesão',
               'Maionese Temperada', 'Mostarda E Mel', 'Supreme']


def remove_ingredientes(ingredientes):
    global listaPaes, listaQueijos, listaVegetais, listaMolhos
    items = ingredientes["Ingredientes"]
    for ingredient in items:
        while ingredient in listaPaes:
            listaPaes.remove(ingredient)
        while ingredient in listaQueijos:
            listaQueijos.remove(ingredient)
        while ingredient in listaVegetais:
            listaVegetais.remove(ingredient)
        while ingredient in listaMolhos:
            listaMolhos.remove(ingredient)

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
