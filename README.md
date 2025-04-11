# BCTEC005_2025_S1_T02---FUNDAMENTOS-DA-PROGRAMA-O-DE-COMPUTADORES
Exercícios do BCTec  FUNDAMENTOS DA PROGRAMAÇÃO DE COMPUTADORES

# Tutoria 4 - Estruturas de Decisão 🧠🔍

**Universidade Federal de Itajubá – UNIFEI**  
**Curso:** Bacharelado em Ciência e Tecnologia (BCTec)  
**Disciplina:** Fundamentos da Programação de Computadores  
**Módulo:** 2  
**Professor:** Fischer Ferreira  
**Tutoria 4:** Estruturas de Decisão  
**Objetivo:** Desenvolver estruturas de decisão aninhadas complexas, avaliando múltiplos critérios para tomar decisões lógicas baseadas em diversas variáveis.

---

## 🧭 Contexto Narrativo

Alex, o explorador digital, chegou ao **Salão do Guardião Lógico**, onde deverá provar sua maestria em **estruturas de decisão**. Somente ao decifrar todas as combinações lógicas, será capaz de acessar o **Coração do Código**. Para isso, precisará interagir com o sistema de decisão e lidar com parâmetros variados.

---

## 🔢 Parâmetros de Entrada

1. `qualificacao` — deve ser múltiplo de 4 e entre 1 e 100  
2. `energia` — entre 0 e 100 e deve ser ≥ (30 + qualificacao × 0.6)  
3. `tem_chave_mestra` — booleano (`sim` ou `não`, convertido para `True` ou `False`)  
4. `localizacao` — apenas um dos três: `floresta`, `caverna` ou `torre`  
5. `inteligencia` — calculada conforme regras abaixo  
6. `confiabilidade_sistema` — inicia em 50 e depende da qualificação e localização  
7. `mapa_templo` — inteiro e **par**

---

## 🔁 Regras de Lógica – Grupo 1: Restrições

- A energia depende da qualificação do personagem.
- A inteligência mínima necessária depende de vários fatores:  
  `inteligencia_minima = 40 + (0.3 × qualificacao) + (0.2 × energia) - (0.1 × confiabilidade) + 10 (se não tiver o mapa)`
- A confiabilidade é iniciada em 50 e ajustada com:  
  `+ 0.4 × qualificacao`  
  `- 10 (se localizacao == 'floresta')`

---

## 🧠 Regras de Decisão – Grupo 2: Missões por Localização

### 🌲 Floresta:
- Energia < 20, qualificação > 50, inteligência ∈ [40, 70] → _"Missão: Recolher fragmentos de código perdidos."_  
- Energia ∈ [20, 60], inteligência < 70, confiabilidade < 50 → _"Missão: Resolver enigmas lógicos para ganhar sabedoria."_  
- Energia > 60 **ou** energia < 30 → _"Missão: Evacuar a floresta imediatamente. Situação crítica."_  
- Caso contrário → _"Missão: Encontrar a saída da floresta e seguir para a caverna."_

### 🕳️ Caverna:
- Energia < 40, qualificação > 60, sem mapa → _"Missão: Recuperar energia em uma estação escondida."_  
- Inteligência > 90, com mapa → _"Missão secreta desbloqueada: acessar arquivos ocultos."_  
- Energia ∈ [40, 70], qualificação < 30 → _"Missão: Treinar lógica em painéis antigos da caverna."_  
- Senão → _"Aguarde reforço ou procure por dicas nos cantos da caverna."_

### 🗼 Torre:
- Confiabilidade < 40, inteligência < 60 → _"Missão: Verificar sistemas danificados da torre."_  
- Sem chave mestra, energia ≥ 80 → _"Missão: Encontrar a Chave Mestra escondida nos arquivos antigos."_  
- Energia > 85, qualificação > 90, inteligência > 95 → _"Missão final desbloqueada: Acesse o Julgamento Supremo."_  
- Caso contrário → _"Missão concluída! Você está pronto para o Julgamento Final."_

---

## 🧩 Regras de Decisão – Grupo 3: Situações Estratégicas

### Alta Energia (> 80), Alta Qualificação (> 70) e Chave Mestra:
- Se confiabilidade < 50 → _"Aguardar verificação de integridade antes de prosseguir"_  
- Se inteligência ≥ 80 **e** localização = torre → _"Acesso permitido ao Templo final"_  
  - Senão → _"Redirecionar para torre para verificação."_  
  - Se inteligência < 80 → _"Participe mais das tutorias"_  
- Localização = floresta → _"Vá para a torre"_  
- Localização = caverna → _"Vá para a floresta"_

### Energia entre 50 e 80:
- Se energia < 40 → _"Vá para a zona de treinamento."_  
- Se energia suficiente e tem chave → _"Vá para um desafio intermediário"_  
- Senão → _"Você precisa recuperar a chave ou energia"_  
- Se inteligência > 80, confiabilidade > 50 → _"Você ainda está na briga!"_

### Energia < 50:
- Floresta → _"Você precisa explorar mais."_  
- Caverna → _"Dica: procure sabedoria entre as pedras. Missão reiniciada."_  
- Outro → _"Enviar para a zona de teste."_  
- Se energia > 2, inteligência > 80, confiabilidade > 50 → _"Seus níveis de energia ainda dá para brigar!"_  
  - Senão → _"Fim de jogo"_

---

## 🧬 Regras de Decisão – Grupo 4: Ajustes e Conclusões

- Energia ∈ [30, 60], inteligência ∈ [60, 90], qualificação > 50, confiabilidade ∈ [40, 70] →  
  _"Você está em ascensão! Foque em melhorar sua lógica e energia."_  
  - Senão → _"Você está no caminho certo, mas encontre o Mapa do Templo para evoluir com precisão."_

- Energia < 30, confiabilidade < 40, qualificação > 35, inteligência < 50 →  
  _"Atenção: Você está em uma zona de risco. Evite decisões precipitadas."_  
  - Senão → _"Atenção: Você está em uma zona de risco. Evite decisões precipitadas e busque suporte."_

- Energia > 90, inteligência > 85, qualificação > 80, chave_mestra = True, confiabilidade > 60 →  
  _"Parabéns! Você atingiu o nível de energia de excelência para o Desafio Supremo. Prepare-se!"_  
  - Senão, se sem mapa → _"Você está pronto, mas precisa do Mapa do Templo para acessar o Desafio Supremo."_

- Se localização = torre → _"Parabéns! Você atingiu o nível de energia de excelência para o Desafio Supremo."_  
  - Senão → _"Dirija-se imediatamente à torre para acessar o Desafio Supremo."_

- Energia < 25 e sem mapa → _"Seu progresso está comprometido. Recupere energia e encontre o Mapa do Templo."_

- Nenhuma condição satisfeita → _"Continue explorando e aprimorando seus atributos. Sua hora vai chegar!"_

---

## 🧰 Requisitos Técnicos

- Linguagem: Python (sugestão)
- Uso intensivo de `if`, `elif`, `else` e expressões booleanas
- Organização modular do código é recomendada
- Validação de entradas deve ser implementada com robustez

---
