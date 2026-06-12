def caixa():

    print("\n------Cálculo de Troco------\n")
    cedulas_moedas = [
        ("R$ 200,00", 20000),
        ("R$ 100,00", 10000),
        ("R$ 50,00", 5000),
        ("R$ 20,00", 2000),
        ("R$ 10,00", 1000),
        ("R$ 5,00", 500),
        ("R$ 2,00", 200),
        ("R$ 1,00", 100),
        ("R$ 0,50", 50),
        ("R$ 0,25", 25),
        ("R$ 0,10", 10),
        ("R$ 0,05", 5),
        ("R$ 0,01", 1)
    ]

    while True:
        try:
            valor_compra = float(input("Digite o valor da compra: "))
            if valor_compra <= 0:
                print("Digite um valor válido!")
                continue
            valor_pago = float(input("Digite o valor pago pelo cliente: "))
            if valor_pago <= 0:
                print("Digite um valor válido!")
                continue

            if valor_pago < valor_compra:
                print("\nValor insuficiente para pagar a compra!")
                continue

            troco = valor_pago - valor_compra
            restante = round(troco * 100) # Coloca o valor restante em centavos, para facilitar calculos

            print("\n======Info de Compra======\n")
            print(f"Valor total das compras: R${valor_compra:.2f}")
            print(f"Valor recebido do cliente: R${valor_pago:.2f}")
            print(f"Valor do troco: R${troco:.2f}")
            print("\nNotas necessárias para dar o troco ao cliente: ")


            # Percorre a lista de cédulas e moedas disponíveis
            for nome, valor in cedulas_moedas:
                quantidade = restante // valor

                if quantidade > 0:
                    print(f"{quantidade} x {nome}")

                restante %= valor

            print("\n")
            input("Digite qualquer valor para voltar ao Menu...")
            break         
        except ValueError:
            print("\nDigite algo válido!")
            return 0