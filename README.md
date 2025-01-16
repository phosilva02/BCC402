# BCC402

Exercícios referentes a disciplica BCC402 - Algoritmos e Programação Avançada, Período 24/2

Atividade 01 -> 1.6.5 Graphical Editor

Atividade 02 -> 2.8.5 Stack'em Up

Atividade 03 -> 3.8.5 Automated Judge Script

Atividade 04 -> 4.6.5 Shoemaker's Problem

## Atividade 01 -> 1.6.5 Graphical Editor

### Pseudo Código

```plaintext
Inicio
    Enquanto não for fim de comandos
        Leia Comando
        Se comando for válido
            Executa comando
        Senão
            Exibe que comando não é valido
        Fim Se
    Fim Enquanto
Fim
```

### Testes

Execute ```python3 -m tests.testGraphicalEditor``` para rodar os testes.

## Atividade 02 -> 2.8.5 Stack'em Up

### Pseudo Código

```plaintext
Inicio
    Leia numeroCasos
    Enquanto case for menor que numeroCasos
        Baralho <- Baralho Inicializado
        Leia numeroEmbaralhadas
        tiposEmbaralhadas <- Lista Vazia
        Enquanto i for menor que numeroEmbaralhadas
            Enquanto j for menor que 52
                Leia embaralhada = posição das cartas no baralho
                j <- j+1
            Fim Enquanto
            insira embaralhada em tiposEmbaralhadas
            i <- i+1
        Fim Enquanto
        ordemEmbaralhadas <- Lista Vazia
        Enquanto digitar numero inteiro
            insira numero digitado em ordemEmbaralhadas
        Fim Enquanto
        Para k em ordemEmbaralhadas
            embaralhada <- elemento k-1 da lista tiposEmbaralhadas
            baralhoProvisorio <- Lista Vazia
            Para pos em embaralhada
                carta <- obter elemento no indice pos em Baralho
                insira carta em baralhoProvisorio
            Fim Para
            Baralho <- baralhoProvisorio
        Fim Para
        case <- case+1
    Fim Enquanto
Fim
```

### Testes

Execute ```python3 -m tests.testStackemUp``` para rodar os testes.

## Atividade 03 -> 3.8.5 Automated Judge Script

### Pseudo Código

```plaintext
Inicio
    cont <- 1
    Enquanto Verdadeiro
        Ler n
        Se n for menor ou igual a 0:
            Sair do loop
        Fim Se
        standardSolution <- Lista Vazia
        Para i de 0 até n-1:
            Ler resposta
            adicionar resposta à lista standardSolution
        Fim Para
        Ler m
        teamOutput <- lista vazia
        Para i de 0 até m-1:
            Ler resposta
            adicionar resposta à lista teamOutput
        Fim Para
        JudgeAnswers <- lista vazia
        Para i de 0 até n-1:
            correctAnswer <- Elemento i de standardSolution
            teamAnswer <- Elemento i de teamOutput
            Se correctAnswer for totalmente igual a teamAnswer:
                adicionar "Accepted" à lista JudgeAnwsers
            Senão se numeros de correctAnswer forem iguais ao numeros de teamAnswer:
                adicionar "Presentation Error" à lista JudgeAnwsers
            Senão:
                adicionar "Wrong Answer" à lista JudgeAnwsers
            Fim Se
        Fim Para
        remover duplicatas de JudgeAnwsers
        Se "Wrong Answer" estiver em JudgeAnwsers:
            finalAnwser <- "Run #cont: WrongAnswer"
        Senão se "Presentation Error" estiver em JudgeAnwsers:
            finalAnwser <- "Run #cont: Presentation Error"
        Senão:
            finalAnwser <- "Run #cont: Accepted"
        Fim Se
        imprimir finalAnwser
        cont <- cont+1
    Fim Enquanto
Fim
```

### Testes

Execute ```python3 -m tests.testAutomatedJudge``` para rodar os testes.

## Atividade 04 -> 4.6.5 - Shoemaker's Problem

### Pseudo Código

```plaintext
Inicio
    ler numCases
    Para i de 0 até numCases-1
        Ler n
        Converter n para inteiro
        orders <- lista vazia
        Para j de 0 até n-1:
            Ler order
            Adicionar order à lista orders
        Fim Para
        Ordenar orders usando a fórmula de comparação: chave = order[0] (Data de vencimento) / order[1] (Valor de multa)
        Imprimir orders ordenada
    Fim Para
Fim
```

### Testes

Execute ```python3 -m tests.testShoemaker``` para rodar os testes.

## Atividade 05 -> 5.9.5 - A Multiplication Game

### Pseudo Código

```plaintext
Inicio
    Ler n
    Inicializar p como 1
    Inicializar turn como 0
    Inicializar mult como 2
    Inicializar values como lista [9, 8, 7, 6, 5, 4, 3, 2]
    Enquanto (p * 9) < n:
        Para cada div em values:
            Se n / (p * div) <= 9:
                Se div for igual a 2:
                    Definir mult como 2
                Fim Se
                Continuar para o próximo div
            Fim Se
            Definir mult como div
            Sair do loop
        Fim Para
        Multiplicar p por mult
        Incrementar turn em 1
    Fim Enquanto
    Se turn for ímpar:
        Imprimir "Ollie wins."
    Senão:
        Imprimir "Stan wins."
Fim
```

### Testes

Execute ```python3 -m tests.testMultiplicationGame``` para rodar os testes.