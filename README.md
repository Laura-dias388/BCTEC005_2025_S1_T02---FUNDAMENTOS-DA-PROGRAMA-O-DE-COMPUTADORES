# BCTEC005_2025_S1_T02---FUNDAMENTOS-DA-PROGRAMA-O-DE-COMPUTADORES
Exercícios do BCTec  FUNDAMENTOS DA PROGRAMAÇÃO DE COMPUTADORES
# Introdução as estruturas condicionais if, elif e else.


<details>
  <summary><strong>Informações:</strong></summary><br />

  If... Else
A tomada de decisão é necessária quando queremos executar um código apenas se uma determinada condição for satisfeita.

As instruções if, elif e else são usadas em Python para nos auxiliar na tomada de decisões.
<img src="Captura de tela 2025-04-04 055938.png" alt="Fluxograma de estrutura condicional">

</details>

<details>
  <summary><strong>Material sobre if, elif e else</strong></summary><br />

 tomada de decisão é um conceito muito importante da programação e representa a capacidade de executarmos determinados comandos apenas se condições especificadas forem satisfeitas.

Lembrando que Python é capaz de suportar as condições lógicas tradicionais da matemática:

Igualdade: x == y
Diferente de: x != y
Menor que: x < y
Menor que ou igual a: x <= y
Maior que: x > y
Maior que ou igual a: x >= y
Essas condições podem ser usadas de várias maneiras, e são comumente utilizadas em instruções if e loops.

A sintaxe para construirmos uma estrutura de tomada de decisão funciona então da seguinte forma:

 <img src="Captura de tela 2025-04-04 060407.png" alt="Explicação de estrutura condicional">

Para mais detalhes consulte:

https://pythoniluminado.netlify.app/if-else
</details>

<details>
<summary><strong>Exercício Estruturas de decisão</strong></summary><br />

Após atravessar os Salões das Variáveis, Alex chega a uma nova área do Templo da Programação: a Câmara das Escolhas.  
Diante dele, três portões digitais brilham em cores diferentes. Uma placa antiga revela:

> “Apenas quem domina o poder da decisão lógica poderá seguir adiante.”

Sua missão agora é ajudar Alex a analisar situações, criar condições e executar diferentes caminhos de acordo com o que o programa encontrar.

---

### 🧭 Fase 1: Entrada na Câmara das Escolhas

> **Pergunta:** Você quer entrar na Câmara das escolhas? (sim ou não)

- Se a escolha for **sim**: imprima `bora lá!`
- Se a escolha for **não**: imprima `volte para fase das variáveis!`

---

### 🔐 Fase 2: Desbloqueio de Portões Lógicos

> **Pergunta:** Quantas chaves mágicas você coletou?

- **3 chaves** → `Portão de bronze aberto!`
- **5 chaves** → `Portão de prata aberto!`
- **7 chaves** → `Portão de ouro aberto!`
- **Outro número** → `Número incorreto de chaves. Portão permanece fechado.`

---

### 💪 Fase 3: Verificação do Nível de Força

> **Variável:** nível de força do personagem

- Se **nível > 100** → `Níveis aceitáveis de força`
- Se **nível <= 100** → `Precisa estudar mais para melhorar seus níveis de força`

---

### 🌀 Fase 4: Escolha do Caminho no Labirinto

> **Escolha:** floresta, caverna ou rio

- **floresta** → `Você foi atacado por robôs-programadores. Volte ao início.`
- **caverna** → `Você encontrou um enigma lógico!`
- **rio** → `Você atravessou com sucesso para a próxima fase!`
- **Qualquer outro** → `Caminho inválido. Tente novamente.`

---

### 🔒 Fase 5: Cofre Codificado com Adivinhação

> A senha secreta é `7`  
> **Pergunta:** Tente adivinhação

> A senha secreta é `7`  
> **Pergunta:** Tente adivinhar a senha entre 1 e 10

- Se for **igual** → `Senha correta! Cofre aberto.`
- Se for **menor** → `Senha muito baixa.`
- Se for **maior** → `Senha muito alta.`

---

### 🌡️ Fase 6: Termômetro de Temperatura Digital

> **Pergunta:** Digite a temperatura atual

- **≤ 25** → `Temperatura ideal. Robô funcionando.`
- **< 15** → `Muito frio! Robô congelado.`
- **> 25** → `Muito quente! Robô superaquecido`

---

</details>


