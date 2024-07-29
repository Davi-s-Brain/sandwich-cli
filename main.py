import typer
import inquirer
import randomizer
from rich import print


def main():
    escolha_remove_ingredients = inquirer.list_input(
        "Deseja remover algum item? (S/N)", choices=["Sim", "Nao"])

    remove_ingredients = [
        inquirer.Checkbox(
        "Ingredientes",
        message="Quais ingredientes você deseja remover?",
        choices=['3 Queijos', 'Parmesão E orégano', '9 grãos', 'Italiano Branco', 'Cheddar', 'Suíço', 'Queijo Mussarela Ralada', 'Azeitonas', 'Picles', 'Pepinos',
                 'Pimentão', 'Alface', 'Cebola Roxa', 'Tomate', 'Rúcula', 'Cebola Agridoce', 'Chipotle', 'Barbecue', 'Parmesão', 'Maionese Temperada', 'Mostarda E Mel', 'Supreme'],
        default=[]
        )
    ]

    if escolha_remove_ingredients == 'Sim':
        answers = inquirer.prompt(remove_ingredients)
        print(answers)
        randomizer.remove_ingredientes(answers)

    bread = randomizer.escolhe_pao()
    cheese = randomizer.escolhe_queijo()

    remove_vegetais = inquirer.list_input(
        "Deseja escolher a quantidade de vegetais? (S/N) ", choices=["Sim", "Nao"])
    if remove_vegetais == 'Sim':
        quantidade_ingrediente = inquirer.text(
            message="Quantos vegetais você deseja remover? (1/4)")
        vegetables = randomizer.escolhe_vegetais(int(quantidade_ingrediente))
    else:
        vegetables = randomizer.escolhe_vegetais(quantidade_vegetais=-1)


    remove_molhos = inquirer.list_input(
        "Deseja escolher a quantidade de molhos? (S/N)", choices=["Sim", "Nao"])
    if remove_molhos == 'Sim':
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
