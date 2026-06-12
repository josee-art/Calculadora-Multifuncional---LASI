def posicao_da_queda():

    print("\n------Física 1: Cálculo da posição da queda de um projetíl------\n")

    try:
        v0 = float(input("Digite a velocidade inicial (m/s): "))
        if v0 < 0:
            print("\nA velocidade inicial não pode ser menor que zero!")
            return 0
            
        angulo = float(input("Digite o ângulo de lançamento (0, 30, 45 ou 60): "))
        
        y0 = float(input("Digite a altura inicial (m, deve ser > 0 se o ângulo for 0): "))
        if y0 < 0:
            print("\nAltura inicial não pode ser negativa!")
            return 0 
            
        # Impede ângulo 0 ou velocidade 0 direto no chão
        if (angulo == 0 or v0 == 0) and y0 == 0:
            print("\nPara ângulo ou velocidade zero, a altura inicial deve ser maior que zero!")
            return 0

        g = float(input("Digite a gravidade (m/s²): "))
        if g <= 0:
            print("\nO valor da aceleração da gravidade deve ser maior que zero!")
            return 0
            
    except ValueError:
        print("\nDigite um valor numérico válido!")
        return 0

    # DEFINIÇÃO DAS COMPONENTES BASEADO NO ÂNGULO DIGITADO
    if angulo == 0:
        sen = 0.0
        cos = 1.0
    elif angulo == 30:
        sen = 0.5
        cos = 0.866
    elif angulo == 45:
        sen = 0.707
        cos = 0.707
    elif angulo == 60:
        sen = 0.866
        cos = 0.5
    else:
        angulo = float(45)
        print("\nÂngulo inválido para esta tabela! Definindo padrão de 45 graus.")
        sen = 0.707
        cos = 0.707

    # COMPONENTES DA VELOCIDADE
    v0_x = v0 * cos
    v0_y = v0 * sen

    # ALTURA MÁXIMA
    altura_maxima = y0 + (v0_y ** 2) / (2 * g)

    # TEMPO DE VOO (Bhaskara pura: a*t² + b*t + c = 0)
    a = -0.5 * g
    b = v0_y
    c = y0

    delta = b**2 - 4*a*c

    if delta < 0:
        print("\nNão existe solução real para o movimento.")
        return 0

    raiz1 = (-b + delta**0.5) / (2*a)
    raiz2 = (-b - delta**0.5) / (2*a)

    tempo_voo = max(raiz1, raiz2)
    if tempo_voo <= 0:
        print("\nNão foi possível determinar um tempo de voo válido.")
        return 0
    alcance = v0_x * tempo_voo
    
    print("\n--- RESULTADOS DO LANÇAMENTO ---")
    if v0 == 0:
        print("* Nota: Objeto abandonado em Queda Livre Vertical.")
    elif angulo == 0:
        print("* Nota: Lançamento perfeitamente Horizontal.")
        
    print(f"Tempo total de voo: {tempo_voo:.2f} segundos")
    print(f"Altura máxima atingida: {altura_maxima:.2f} metros")
    print(f"Posição da queda (Alcance horizontal): {alcance:.2f} metros do ponto inicial")
   
    input("Digite qualquer valor para voltar ao Menu...")
