# BCTEC005_2025_S1_T02---FUNDAMENTOS-DA-PROGRAMA-O-DE-COMPUTADORES
Exercícios do BCTec  FUNDAMENTOS DA PROGRAMAÇÃO DE COMPUTADORES
# Introdução às Estruturas de Repetição  
**Fundamentos da Programação de Computadores**  
**Prof: Fischer Ferreira**

---

## 🧭 Introdução

Depois de dominar as escolhas lógicas na Câmara das Decisões, Alex segue mais fundo no Templo da Programação e chega a um novo salão: **a Galeria dos Laços Infinitos**.  

Nas paredes, inscrições antigas dizem:  
> “Apenas quem souber controlar a repetição dos ciclos poderá avançar pelo templo.”

Aqui, Alex precisará aprender a usar **estruturas de repetição** como `while` e `for` para superar os desafios.  
Sua missão agora é ajudar Alex a construir repetições controladas para conquistar cada etapa da galeria.

---

## 🗝️ Fase 1: O Portal das Perguntas

**Descrição:**  
Alex encontra um portal que só se abre se ele responder "sim" a uma pergunta.

**Requisitos do programa:**
- Pergunte: `"Você deseja continuar a jornada? (sim/não)"`
- Enquanto a resposta for diferente de `"sim"`, imprima:
  > `"Resposta inválida para avançar. Tente novamente!"`
- Quando a resposta for `"sim"`, imprima:
  > `"Portal aberto! Você pode seguir em frente."`

---

## 🧗‍♂️ Fase 2: A Subida da Escada Infinita

**Descrição:**  
Alex chega a uma escada mágica que só desaparece quando ele atingir o degrau informado pelo jogador.

**Requisitos do programa:**
- Comece no degrau 1 e vá subindo (`while`) até o degrau limite informado.
- Em cada degrau, pergunte se é o degrau secreto.
- Para cada degrau, imprima:
  > `"Estou no degrau y"`
- Informe se o degrau é o mesmo informado pelo jogador.
- Ao chegar ao topo, imprima:
  > `"Você chegou ao topo da escada!"`

---

## 💎 Fase 3: A Contagem das Pedras Luminosas

**Descrição:**  
Alex precisa coletar pedras mágicas em 10 pontos da galeria.

**Requisitos do programa:**
● Imprima a coleta de cada pedra usando uma repetição (for).
● Para cada ponto de coleta imprima: quantas pedras foram coletadas? apresente o total de 
pedras coletadas por ponto de coleta imprima: `"Ponto de coleta: x - número de pedras coletadas: y!"` (substituindo: x pelo ponto de coleta y pelo número da pedra, da iteração).
● Ao final, imprima: `"O total de pedras luminosas foram coletadas!`

---

## 🧮 Fase 4: Escolha do Caminho no Labirinto

**Descrição:**  
Alex precisa gerar as tabuadas mágicas de 1 até 10 usando `while` aninhados.

**Requisitos do programa:**
● Para cada número de 1 a 10 (representando as tábuas mágicas),
● Alex precisa listar a multiplicação de 1 a 10 para cada número.
● Use dois while aninhados:
○ O while externo controla o número da tabuada (1 até 5).
○ O while interno gera a multiplicação de 1 a 10 para cada número.
---

## 🔐 Fase 5: Cofre Codificado com Adivinhação

**Descrição:**  
Alex precisa acertar o número da chave e o código de segurança para abrir o cofre.

**Requisitos do programa:**
● Pergunte para Alex: 
  > `"Digite o número da chave (entre 1 e 10):"`
● Enquanto a chave não for correta, continue perguntando.
● Quando acertar a chave correta, entre em um novo while:
● Pergunte:
  > `"Digite o código de segurança:"` Enquanto o código não for correto, continue perguntando.
● Quando acertar o código, imprima: 
  > `"Cofre aberto com sucesso! Tesouro liberado!`

**Dica:**

import random
numero_aleatorio = random.randint(1, 10)

## 🌬️ Fase 6: O Enigma dos Dois Caminhos
**Descrição:**
Dois caminhos mágicos se cruzam. A missão é encontrar o ponto de equilíbrio.

**Requisitos do programa:**

● Inicialize x com 100 e y com 1.
● Utilize dois while aninhados:
● O primeiro while decrementa x de 1 em 1.
● Dentro dele, um segundo while incrementa y de 1 em 1.
● A condição para parar os dois laços é: Equação mágica: **x + 2 * y = 150**
● Quando a equação for satisfeita, imprima:
   > `"Equilíbrio encontrado: imprima o valores de x e y"`.
E finalize o programa.

## 🚪 Fase 7: O Portal dos Dois Guardiões
**Descrição:**
Alex precisa satisfazer duas condições mágicas ao mesmo tempo para abrir o portal.

**Requisitos do programa:**

Faça um programa para o valor de x varie de 100 até 1 e y varie de 1 até 100, faça isso até que: 
● A diferença absoluta entre x e y seja menor que **5: (x - y)< 5**
● O produto de x por y seja um número maior que **3000: (x * y > 3000)**

## 🌌 Fase 8: O Santuário das Constelações
**Descrição:**
Alex precisa coletar gemas em constelações, mas com energia limitada.

**Requisitos do programa:**

● Visitar 10 constelações diferentes.
● Em cada constelação, coletar pelo menos 5 gemas.
● Só que há um desafio extra: Alex tem uma energia limitada. 
● Ele começa com energia = 100.
● Cada vez que ele coleta uma gema, perde 2 pontos de energia.
● Se a energia de Alex chegar a zero ou menos, ele não pode mais coletar.

## ⚔️ Fase 9: A Batalha contra o Guardião dos Códigos
**Descrição:**
Alex enfrenta um guardião com múltiplas camadas de proteção.

**Requisitos do programa:**

- Alex começa com força 100.
- Guardião tem 3 camadas, cada uma com 50 de resistência.
- A cada ataque:
- Alex perde 5 de força.
- 30% de chance do ataque falhar.
- Se acertar, camada perde 10.
- Vitória: destruir as 3 camadas.
- Derrota: força de Alex chega a 0.

  > `Derrotar o guardião dos códigos é sua missão, vamos!!`