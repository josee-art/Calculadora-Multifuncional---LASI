from fisica import posicao_da_queda

def Menu():

    print("\n=====Calculadora Multifuncional=====\n\n")
    print("1 - Expresões matemáticas")
    print("2 - Cálculo da posição da queda de um objeto")
    print("3 - OUTRA FUNÇÃO")
    print("4 - Sair do Programa")
    try:
        opcao = int(input("\nDigite a opção desejada: "))
        return opcao
    except ValueError:
        return 0

def Expressao():
    try:
        resultado = float(input("Digite o valor inicial: "))

        while True:

            print(f"\nResultado atual: {resultado}")
            print("Escolha uma das funções abaixo para continuar sua expressão: ")
            print("1 - Somar")
            print("2 - Subtrair")
            print("3 - Multiplicar")
            print("4 - Dividir")
            print("5 - Voltar ao menu principal")

            try:
                opcao = int(input("Escolha uma operação: "))

                if opcao == 5:
                    break

                valor = float(input("Digite o valor: "))

                if opcao == 1:
                    resultado = soma(resultado, valor)

                elif opcao == 2:
                    resultado = subtracao(resultado, valor)

                elif opcao == 3:
                    resultado = multiplicacao(resultado, valor)

                elif opcao == 4:
                    try:
                        resultado = divisao(resultado, valor)
                    except ValueError as erro:
                        print(erro)

                else:
                    print("Opção inválida.")
            except ValueError:
                print("\nDigite uma opção válida!")
                continue

        print(f"\nResultado final da expressão: {resultado}")
    except ValueError:
        print("\nDigite um valor válido!")
        return 0

def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a/b

while True:
    opcao = Menu()

    if opcao == 1:
        Expressao()
    
    elif opcao == 2:
        posicao_da_queda()
    
    elif opcao == 4:
        print("\nEncerrando sistema...")
        break

    else:
        print("\nDigite uma opção válida!")