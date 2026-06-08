# Calculadora Multifuncional - LASI



###### **Descrição:**



&#x20;Este projeto consiste em uma calculadora multifuncional desenvolvida em Python utilizando apenas recursos básicos da linguagem. O programa reúne diferentes funcionalidades em um único sistema de menu interativo, permitindo ao usuário realizar cálculos matemáticos, resolver problemas de Física relacionados ao lançamento de projéteis e calcular trocos para operações de caixa.



&#x20;Além dos cálculos, o sistema registra os resultados em arquivos de histórico para consulta posterior.



##### **Estrutura do Projeto**

O programa está dividido em módulos independentes:

* &#x20;calculadora multifuncional.py -> Responsável pelo menu principal e pela calculadora de expressões matemáticas;
* física.py -> Responsável pelo cálculo da posição de queda de um projétil;
* fluxo\_de\_caixa.py -> Responsável pelo cálculo de troco.



##### **Funcionalidade 1:** 

##### &#x20;**Calculadora de Expressões Matemáticas**



###### **Objetivo:**

&#x20;Permitir que o usuário construa uma expressão matemática passo a passo utilizando operações básicas.



###### **Algoritmo:**

&#x20;Inicialmente o usuário fornece um valor inicial, o programa armazena esse valor na variável resultado.

&#x20;Em seguida, um laço de repetição permite que o usuário escolha sucessivamente uma das seguintes operações:

* Soma
* Subtração
* Multiplicação
* Divisão

&#x20;Após cada operação:

1. O usuário informa um novo valor
2. A operação escolhida é executada
3. O resultado é atualizado
4. O novo resultado é exibido na tela

&#x20;O processo continua até que o usuário escolha retornar ao menu principal



###### **Tratamento de Erros**

&#x20;A divisão por zero é tratada através de exceções (try/except), impedindo que o programa seja encerrado abruptamente.



##### **Funcionalidade 2:**

##### &#x20;**Cálculo da Posição da Queda de um Projétil**



###### **Objetivo:**

&#x20;Determinar as principais características de um lançamento oblíquo:

* Tempo total de voo
* Altura máxima atingida
* Alcance horizontal



###### **Algoritmo:**

&#x20;O usuário informa:

* Velocidade Inicial
* Ângulo de lançamento
* Altura inicial
* Valor da gravidade



&#x20;O programa utiliza decomposição vetorial para separar a velocidade inicial em duas componentes:



&#x20;                 Componente Horizontal: v0x = v0 × cos(θ)

&#x20;                 Componente Vertical: v0y = v0 × seno(θ)



&#x20;Como não foram utilizadas bibliotecas matemáticas, os valores de seno e cosseno são definidos manualmente para ângulos específicos, 0, 30,45 e 60 graus.



&#x20;A altura máxima é calculada utilizando a equação da energia cinemática:



&#x20;                  hmax = y0 + (v0y² / 2g)



&#x20;O movimento vertical é modelado pela equação:



&#x20;                  y = y0 + v0y·t − (g·t²)/2



&#x20;Ao considerar o momento da queda (y = 0), obtém-se uma equação do segundo grau. É necessário aplicar a Fórmula de Bhaskara para encontrar as raízes da equação e selecionar o tempo fisicamente válido:



&#x20;                  raiz1 = (-b + delta\*\*0.5) / (2\*a)

&#x20;                  raiz2 = (-b - delta\*\*0.5) / (2\*a)

&#x20;                  tempo\_voo = max(raiz1, raiz2)



&#x20;Após determinar o tempo total de voo: 



&#x20;                  alcance = v0x × tempo\_voo

&#x20;

&#x20;O resultado representa a posição da queda em relação ao ponto inicial.



##### **Funcionalidade 3:**

##### &#x20;**Cálculo da Troco**



###### **Objetivo:**

&#x20;Determinar o valor do troco e informar quais notas e moedas devem ser utilizadas para devolvê-lo ao cliente.



###### **Algoritmo:**

&#x20;O usuário informa:

* Valor da compra
* Valor pago

&#x20;O programa calcula: troco = valor\_pago - valor\_compra

&#x20;Para evitar erros de precisão causados por números decimais, o valor do troco é convertido para centavos.

&#x20;Exemplo:

&#x20;R$ 62,65 → 6265 centavos

&#x20;Após isso, o algoritmo percorre uma lista contendo todas as notas e moedas disponíveis em ordem decrescente:

&#x20;cedulas\_moedas = \[

&#x20;       ("R$ 200,00", 20000),

&#x20;       ("R$ 100,00", 10000),

&#x20;       ("R$ 50,00", 5000),

&#x20;       ("R$ 20,00", 2000),

&#x20;       ("R$ 10,00", 1000),

&#x20;       ("R$ 5,00", 500),

&#x20;       ("R$ 2,00", 200),

&#x20;       ("R$ 1,00", 100),

&#x20;       ("R$ 0,50", 50),

&#x20;       ("R$ 0,25", 25),

&#x20;       ("R$ 0,10", 10),

&#x20;       ("R$ 0,05", 5),

&#x20;       ("R$ 0,01", 1)

&#x20;   ]

&#x20;Para cada valor:

1. Calcula quantas notas/moedas cabem no valor restante.
2. Exibe a quantidade encontrada
3. Atualiza o restante do troco



&#x20;Exemplo:

&#x20;Troco = 6365 centavos

&#x20;Nota de R$50 (5000 centavos):

&#x20;Quantidade:

&#x20;6265 // 5000 = 1

&#x20;Resto:

&#x20;6265 % 5000 = 1265

&#x20;

&#x20;O processo continua até que o valor restante seja zero

&#x20;

Operadores Utilizados:



&#x20;Divisão inteira: quantidade = restante // valor

&#x20;Resto da divisão: restante %= valor



###### **Histórico de Operações:**

&#x20;Cada módulo registra os resultados em arquivos de texto utilizando:

&#x20;    with open("arquivo.txt", "a", encoding="utf-8")



&#x20;A utilização do modo "a" (append) garante que novos registros sejam adicionados ao final do arquivo sem apagar  os dados anteriores, essa funcionalidade permite acompanhar todas as operações realizadas durante o uso do sistema.



###### **Como executar:**

&#x20;Clone o repositório em alguma pasta no seu computador/notebook, abra a pasta/folder no vscode e execute o arquivo Calculadora\_multifuncional.py



###### **Conclusão:**

&#x20;Este projeto foi desenvolvido com o objetivo de consolidar conhecimentos fundamentais de programação em Python por meio da implementação de problemas matemáticos, físicos e financeiros. A aplicação demonstra a utilização prática de algoritmos, estruturas de controle, manipulação de arquivos e organização modular de código, servindo como uma base sólida para projetos mais avançados.

