# UNIVERSIDADE FEDERAL DE ITAJUBÁ  
### BACHARELADO EM CIÊNCIA E TECNOLOGIA (BCTec)  
**Disciplina:** Fundamentos da Programação de Computadores  
**Trabalho Final**  
**Professor:** Fischer Ferreira  

---

## 🎫 Enunciado do Trabalho Final  
### Sistema de Vendas de Ingressos do Festival de Música BCTec

---

### 📌 Contexto

O festival de música do BCTec requer uma plataforma completa, desenvolvida em **Python**, capaz de gerenciar todo o processo de venda de ingressos: desde o **cadastro de shows** até a **emissão de bilhetes digitais** e a **geração de relatórios administrativos em tempo real**.

---

### 🎯 Objetivo

Implementar um sistema que permita ao usuário:

- Consultar a **disponibilidade de vagas** por dia do festival.
- Selecionar o **setor desejado**.
- Processar o **pagamento**.
- Receber um **bilhete digital personalizado**.
- Registrar todas as informações da venda para **relatórios de acompanhamento**.

---

## 🔧 Descrição das Funcionalidades

Cada show é identificado por:  
- **Nome**, **descrição**, **artista** e **gênero musical**,  
- Associado a um **dia específico do evento**, com:
  - **Data**
  - **Preço-base do ingresso**
  - **Capacidade máxima de público**

O sistema deve:
- Garantir que, ao cadastrar um novo show, a **lotação daquele dia seja respeitada**.
- Impedir vendas acima do limite permitido.

A precificação do ingresso varia conforme o **setor escolhido**, com **capacidade específica**, **percentual de acréscimo** e **brindes correspondentes**.

Formas de pagamento: **PIX (simulado), dinheiro, débito ou crédito**.  
O sistema deve gerar um **bilhete digital** com:

- Nome e data do show
- Setor
- Valor total pago
- Forma de pagamento
- Lista de brindes

---

### 👤 Dados do Cliente

Deve-se solicitar:

- Nome completo
- CPF
- Número de matrícula (opcional)

---

## 🪑 Setores, Acréscimos e Brindes

> *Obs: o número de participantes está reduzido para facilitar testes.*

| Setor         | Vagas | Acréscimo | Brindes                                               |
|---------------|--------|-----------|--------------------------------------------------------|
| Pista         | 4      | 0%        | Nenhum                                                 |
| Campo         | 6      | 10%       | Bonequinho do BCTec                                    |
| Arquibancada  | 5      | 12%       | Bonequinho + Combo de pipoca                           |
| VIP           | 3      | 15%       | Bonequinho + Combo + Refrigerante + Chocolate          |

---

## 🧩 Funcionalidades Detalhadas

### 1. Cadastro de Shows
- Nome, descrição, artista, gênero.
- Associação a um dia (data, preço-base, capacidade).

### 2. Controle de Capacidade
- Atualiza automaticamente a lotação ao vender ou cancelar.
- Bloqueia dias sem vagas.

### 3. Cadastro e Validação de Cliente
- Nome completo, CPF, matrícula (opcional).
- Validação de CPF e campos obrigatórios.

### 4. Seleção de Setor e Cálculo de Preço
- Pista, Campo, Arquibancada, VIP (ver tabela acima).
- Aplicação de acréscimos e registro de brindes.

### 5. Processamento de Pagamento
- Formas: PIX (simulado), dinheiro, débito, crédito.
- Registro da forma de pagamento na transação.

### 6. Emissão de Bilhete Digital
- Dados do cliente
- Nome/data do show
- Setor reservado
- Valor pago
- Forma de pagamento
- Brindes recebidos

### 7. Relatórios Administrativos
- Lista de inscritos por dia.
- Total arrecadado por dia e no evento.
- Quantidade distribuída de:
  - Bonequinhos do BCTec
  - Combos de pipoca
  - Refrigerantes
  - Chocolates

---

## 📏 Critérios de Avaliação

| Critério | Pontos |
|----------|--------|
| Implementação completa das funcionalidades | 2,0 |
| Explicação do código em vídeo (10–15 min), incluindo: nome, matrícula, organização, fluxo, funções e decisões | 10,0 |

---

## 📤 Formato de Entrega

- **Prazo:** até **26 de junho de 2025**
- **Entregar:**
  - Código-fonte em **PDF**
  - Link ou arquivo do **vídeo explicativo**
    - Inicie o vídeo com **gravação do rosto** e **dados de identificação**

---

> **Boa sorte! Capriche na implementação e na explicação!**
