# BCC402

Exercícios referentes a disciplica BCC402 - Algoritmos e Programação Avançada, Período 24/2

Atividade 01 -> 1.6.5 Graphical Editor

Atividade 02 -> 2.8.5 Stack'em Up

Atividade 03 -> 3.8.5 Automated Judge Script

Atividade 04 -> 4.6.5 Shoemaker's Problem

Atividade 05 -> 5.9.5 - A Multiplication Game

Atividade 06 -> 6.6.5 - Complete Tree Labeling

Atividade 07 -> 7.6.5 - Summation of Four Primes

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

## Atividade 06 -> 6.6.5 - Complete Tree Labeling

EM DESENVOLVIMENTO

## Atividade 07 -> 7.6.5 - Summation of Four Primes

### Resumo de Abordagem Utilizada

Baseado na Conjectura de Goldbach, que afirma que todo número par maior que 2 pode ser representado como a soma de dois números primos. A ideia é dividir a entrada na metade, gerando 2 fatores e, para cada numero gerado, fazer o mesmo recursivamente. Se os 2 fatores gerados forem primos, retorna eles. Caso contrário, tira uma unidade de um dos fatores para colocar no outro e repete o processo enquanto ambos os fatores forem maiores ou iguais a 2 (já que 2 é o menor primo). Caso contrário, informa que é impossivel representar esse numero na forma pedida.

### Pseudo Código

```plaintext
Inicio
    Ler entrada do usuário como n
    Se n for menor ou igual a 7:
        Imprimir "Impossible"
        Finalizar processamento
    listaPrimos <-- lista de primos de 2 até n
    result <-- get2Factors(n, listaPrimos, 0)
    Se result for Falso:
        Imprimir "Impossible"
    Senão:
        Imprimir result
Fim

get2Factors(n, listaPrimos, depth):
    Se depth for igual a 2:
        Se n estiver em listaPrimos, retornar n, senão retornar Falso
    a <-- n / 2
    b <-- n - a
    Enquanto b >= 2:
        resultA <-- get2Factors(a, listaPrimos, depth + 1)
        resultB <-- get2Factors(b, listaPrimos, depth + 1)
        Se resultA e resultB não forem Falso:
            Retornar [resultA, resultB]
        a <-- a + 1
        b <-- b - 1
    Fim Enquanto
    Retornar Falso
Fim get2Factors
```

### Testes

Execute ```python3 -m tests.testFourPrimes``` para rodar os testes.

## Atividade 08 -> 8.6.5 - Tug of War

### Resumo de Abordagem Utilizada

Utilizando abordagem de backtracking para a escolha de melhor solução. Quando a solução não é viável, a solução é podada do processamento. O algoritmo de backtracking é baseado no algoritmo aparecido nos slides da disciplina.

Uma solução é viavel se a diferença entre os 2 times ser menor ou igual a 1. Ou seja, a quantidade de pessoas em um time não pode passar da metade do número de pessoas totais

Uma solução é melhor que outra se a diferença absoluta dos pesos entre os times for menor que a diferença absoluta dos pesos dos times formados na solução comparada.

### Pseudo Código

```plaintext
Inicio
    Ler a quantidade de casos
    Para cada caso
        Ler a quantidade de integrantes
        Para cada integrante
            Ler o peso desse integrante e armazenar no vetor de pesos
        Fim Para
        diff <-- soma de todos os pesos
        backTracking()
        Somar os pesos do time 1 baseado na melhor solução dada pelo backtracking
        Somar os pesos do time 2 baseado na melhor solução dada pelo backtracking
        Imprimir pesos do time 1 e do time 2
    Fim Para
Fim

backTracking(depth, solution):
    Se depth é igual a quantidade de integrantes:
        processarSolucao(solution)
    Fim Se
    Senão:
        depth <-- depth + 1
        candidates <-- [1,2]
        Para cada candidato em candidates
            solution[depth] <-- candidato
            Se isViable(solution):
                backTracking(depth, solution)
            Fim Se
        Fim Para
    Fim Senão
Fim backTracking

isViable(solution):
    half <-- divisão inteira do total de integrantes por 2
    Se half >= Quantidade de integrantes do maior time até o momento:
        Retorna Solução viável
    Fim Se
    Senão:
        Retorna Solução inviável
    Fim Senão
Fim isViable

processarSolucao(solucao):
    Separar os times 1 e 2 de acordo com a solução dada
    diffSolucao <-- diferença absoluta de peso entre os 2 times
    Se diffSolucao <= diff
        diff <-- diffSolucao
        melhorSolucao <-- solucao
    Fim Se
Fim processarSolucao

```

### Testes

Execute ```python3 -m tests.testTugOfWar``` para rodar os testes.