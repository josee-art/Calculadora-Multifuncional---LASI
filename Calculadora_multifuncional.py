def Menu():

    print("\n=====Calculadora Muntifuncional=====\n\n")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair do programa")

    try:
        opcao = int(input("\nDigite a opção desejada: "))
        return opcao
    except ValueError:
        return 0

def Soma():

    print("\n-----Função SOMA------\n")
    x = float(input("Digite o primeiro valor: "))
    y = float(input("Digite o segundo valor: "))
    soma = x + y
    print(f"\nO resultado da soma entre {x} e {y} é igual a {soma}\n")
    opcao = input("Digite qualquer valor para voltar ao menu: ")

def Subtracao():

    print("\n-----Função SUBTRAÇÃO------\n")
    x = float(input("Digite o primeiro valor: "))
    y = float(input("Digite o segundo valor: "))
    sub = x - y
    print(f"\nO resultado da subtração entre {x} e {y} é igual a {sub}\n")
    opcao = input("Digite qualquer valor para voltar ao menu: ")


def Multiplicacao():

    print("\n-----Função MULTIPLICAÇÃO------\n")
    x = float(input("Digite o primeiro valor: "))
    y = float(input("Digite o segundo valor: "))
    mul = x * y
    print(f"\nO resultado da multiplicação entre {x} e {y} é igual a {mul}\n")
    opcao = input("Digite qualquer valor para voltar ao menu: ")


def Divisao():

    print("\n-----Função DIVISÃO------\n")
    x = float(input("Digite o valor do numerador: "))
    y = float(input("Digite o valor do denominador: "))
    if y == 0:
        print("\nO denominador não pode ser zero!\n")
        print("\nTente novamente\n")
        y = float(1)
        Divisao()
    else:
        div = x / y
        print(f"\nO resultado da divisão entre {x} e {y} é igual a {div}\n")
        opcao = input("Digite qualquer valor para voltar ao menu: ")


while True:
    opcao = Menu()

    if opcao == 1:
        Soma()

    elif opcao == 2:
        Subtracao()

    elif opcao == 3:
        Multiplicacao()

    elif opcao == 4:
        Divisao()

    elif opcao == 5:
        print("\nEncerrando sistema...")
        break

    else:
        print("\nDigite uma opção válida!")