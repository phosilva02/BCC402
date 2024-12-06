# BCC402

Exercícios referentes a disciplica BCC402 - Algoritmos e Programação Avançada, Período 24/2

Atividade 01 -> 1.6.5 Graphical Editor
Atividade 02 -> 2.8.5 Stack'em Up

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
        Fim Para
        case <- case+1
    Fim Enquanto
Fim
```

### Testes

Execute ```python3 -m tests.testStackemUp.py``` para rodar os testes.