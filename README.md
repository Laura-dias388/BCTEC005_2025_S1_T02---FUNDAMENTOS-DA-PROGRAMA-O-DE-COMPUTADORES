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
- Use um `for` para iterar por 10 pontos de coleta.
- Para cada ponto, imprima:
  > `"Ponto de coleta: x - número de pedras coletadas: y!"`
- Ao final, imprima:
  > `"O total de pedras luminosas foram coletadas!"`

---

## 🧮 Fase 4: Escolha do Caminho no Labirinto

**Descrição:**  
Alex precisa gerar as tabuadas mágicas de 1 até 10 usando `while` aninhados.

**Requisitos do programa:**
- `while` externo: de 1 até 10 (número da tabuada).
- `while` interno: multiplica de 1 até 10.
- Exiba os resultados de cada multiplicação.

---

## 🔐 Fase 6: Cofre Codificado com Adivinhação

**Descrição:**  
Alex precisa acertar o número da chave e o código de segurança para abrir o cofre.

**Requisitos do programa:**
- Pergunte: `"Digite o número da chave (entre 1 e 10):"`
- Enquanto a chave estiver incorreta, repita a pergunta.
- Ao acertar, pergunte:
  > `"Digite o código de segurança:"`
- Quando ambos estiverem corretos, imprima:
  > `"Cofre aberto com sucesso! Tesouro liberado!"`

**Dica:**

import random
numero_aleatorio = random.randint(1, 10)

## 🌬️ Fase 7: O Enigma dos Dois Caminhos
**Descrição:**
Dois caminhos mágicos se cruzam. A missão é encontrar o ponto de equilíbrio.

**Requisitos do programa:**

x começa em 100 e decrementa.
y começa em 1 e incrementa.
Use while aninhados até que:
x + 2 * y == 150
Quando encontrado, imprima:
`"Equilíbrio encontrado: x = X, y = Y"`

## 🚪 Fase 8: O Portal dos Dois Guardiões
**Descrição:**
Alex precisa satisfazer duas condições mágicas ao mesmo tempo para abrir o portal.

**Requisitos do programa:**

x de 100 até 1
y de 1 até 100
Condições:
abs(x - y) < 5
x * y > 3000
`Quando ambas forem verdadeiras, abra o portal.`

## 🌌 Fase 9: O Santuário das Constelações
**Descrição:**
Alex precisa coletar gemas em constelações, mas com energia limitada.

**Requisitos do programa:**

Visite 10 constelações.
Em cada uma, colete 5 gemas.
Energia começa em 100 e diminui 2 por gema.
Pare se energia ≤ 0.

## ⚔️ Fase 10: A Batalha contra o Guardião dos Códigos
**Descrição:**
Alex enfrenta um guardião com múltiplas camadas de proteção.

**Requisitos do programa:**

Alex começa com força 100.
Guardião tem 3 camadas, cada uma com 50 de resistência.
A cada ataque:
Alex perde 5 de força.
30% de chance do ataque falhar.
Se acertar, camada perde 10.
Vitória: destruir as 3 camadas.
Derrota: força de Alex chega a 0.
