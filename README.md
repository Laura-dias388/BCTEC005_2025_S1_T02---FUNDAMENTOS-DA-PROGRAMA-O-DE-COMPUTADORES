# BCTEC005_2025_S1_T02---FUNDAMENTOS-DA-PROGRAMA-O-DE-COMPUTADORES
Exercícios do BCTec  FUNDAMENTOS DA PROGRAMAÇÃO DE COMPUTADORES

## Módulo 4 - Estruturas de repetição
**Prof: Fischer Ferreira**

## Trabalho Prático – Simulador Estatístico de Partidas de Futebol com Pandas e Estruturas de Repetição

Objetivo:
Você deverá construir um programa em Python capaz de analisar partidas de futebol a partir de um **arquivo .csv** e simular o vencedor da partida com base em força de ataque derivada de uma estrutura de repetição. Além disso, o programa deverá realizar análises estatísticas detalhadas da partida utilizando os dados disponíveis na planilha. Este trabalho tem por finalidade exercitar estruturas de repetição **(for, while)**, estruturas de decisão (**if/else)**, uso da biblioteca pandas, e criação de fórmulas personalizadas.

## Fonte de dados:
`Utilize o arquivo partidas_futebol_sem_gols.csv, que contém as seguintes colunas:`
> ● Rodada, TimeCasa, TimeFora

> ● Estatísticas para cada time (time casa e time fora):

> ○ Cartões Amarelos (CA)

> ○ Cartões Vermelhos (CV)

> ○ Chutes a gol

> ○ Escanteios

> ○ Faltas

> ○ Impedimentos

---

## Parte 1: Simulação do placar com base em força de ataque

Para cada linha da planilha (ou uma linha escolhida pelo usuário), simule o placar da partida com base no seguinte algoritmo:


1. Para o time da casa:
   - Sorteie um número inteiro aleatório entre 1 e 100: `limite_forca`.
   - Use uma estrutura de repetição para somar os números de 1 até `limite_forca` (representa a força de ataque).
   - A cada 10 unidades de força, considera-se 1 gol.
> Repita o processo para o time visitante.
2. Indique o time vencedor com base no número de gols simulados. Quem tiver mais gols vence a partida

---

## Parte 2: Estatísticas da Partida

Para a mesma linha (partida), calcule e imprima:


1. **Aproveitamento ofensivo**

A equação do aproveitamento ofensivo (do time) é:

> `aproveitamento = gols simluados X 100 / chutes a gol`

*Atenção: para evitar divisão por zero, verifique se o número de chutes é maior que zero.*

2. **Time mais agressivo**

Agressividade definida por uma fórmula:

> agressividade = (faltas) + 2 X (cartões amarelos) + 3 X (cartões vermelhos)

`Compare o valor de agressividade do time da casa e do visitante, e indique quem foi mais agressivo na partida.`

3. **Comparação de escanteios**

Imprima qual dos dois times teve mais escanteios, ou se houve empate.

> diferença de escanteios = |escanteios casa - escanteios fora|

4. **Pressa ofensiva**

Faça a computação do indice_pressa_ofensiva, representado pela seguinte equação:

> índice de pressa ofensiva (IPO) = impedimentos / chutes a gol + escanteios + 1

A ideia é refletir quantas vezes o time se precipita no ataque, representado pelos impedimentos, em relação às jogadas ofensivas legítimas (chutes a gol e escanteios). Um time muito afobado no ataque tende a se posicionar mal, resultando em mais impedimentos.
---

## Parte 3: Simulação da pressão tática

Para cada time:

1. Sorteie um limite de pressão aleatório entre 50 e 150.
2. Use um `while` para somar a pressão tática fictícia ciclo a ciclo:
- A cada ciclo, adicione um valor fixo (ou variável, conforme implementado).

> pressão + = (escanteios X 1.5) + (chutes a gol X 1.2) - (faltas X 0.5)

3. Pare o loop quando a pressão total ultrapassar o limite de pressão aleatório.
4. Conte quantos ciclos de ataque o time conseguiu manter antes de estourar a pressão máxima.
5. Mostre qual para cada time da partida qual são os valores da pressão tática.

---

## Exigências do trabalho

- Utilizar `pandas` para leitura do arquivo CSV.
- Usar estruturas de repetição (`for`, `while`) e decisões (`if/else`) obrigatoriamente.
- **Não usar funções prontas** para cálculo como `sum()`, `mean()`, etc.
- Computar todas as partidas da planilha.
- O código deve imprimir todas as informações com textos explicativos claros.

---