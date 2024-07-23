import typer
import inquirer
import randomizer
from rich import print


def main():
    remove_ingredients = inquirer.list_input(
        "Deseja remover algum item? (S/N)", choices=["S", "N"])

    randomizer.remove_ingredientes(remove_ingredients)
    bread = randomizer.escolhe_pao()
    cheese = randomizer.escolhe_queijo()

    remove_vegetais = inquirer.list_input(
        "Deseja escolher a quantidade de vegetais? (S/N) ", choices=["S", "N"])
    if remove_vegetais == 'S':
        quantidade_vegetais = inquirer.text(
            message="Quantos vegetais você deseja remover? (1/4)")
        vegetables = randomizer.escolhe_vegetais(int(quantidade_vegetais))
    else:
        vegetables = randomizer.escolhe_vegetais(quantidade_vegetais=-1)

    remove_molhos = inquirer.list_input(
        "Deseja escolher a quantidade de molhos? (S/N) ", choices=["S", "N"])
    if remove_molhos == 'S':
        quantidade_molhos = inquirer.text(
            message="Quantos molhos você deseja remover? (1/4)")
        sauces = randomizer.escolhe_molhos(int(quantidade_molhos))
    else:
        sauces = randomizer.escolhe_molhos(quantidade_molhos=-1)

    print("🍞" + bread)
    print("🧀" + cheese)
    print("🍅" + vegetables)
    print("🥫" + sauces)


if __name__ == "__main__":
    typer.run(main)
