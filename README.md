## UNIVERSIDADE FEDERAL DE ITAJUBÁ
## BACHARELADO EM CIÊNCIA E TECNOLOGIA (BCTec)
Disciplina: Fundamentos da Programação de Computadores
Prof: Fischer Ferreira


## 📄 Descrição

Este repositório contém a implementação do **Trabalho Prático do Módulo 3**, proposto na disciplina **Fundamentos da Programação de Computadores**. O objetivo é aplicar estruturas condicionais (`if`, `elif`, `else`) para resolver problemas lógicos envolvendo as variáveis `A` e `B`.

O trabalho está organizado em **um único arquivo Python**, com **10 itens distintos**, separados por comentários numerados.

# Tabalho Prático Módulo 3
➡️Implemente um programa em Python que contenha os itens abaixo. Faça apenas um
arquivo com cada item separado por um comentário com a numeração do item.

---

## 🧠 Estrutura do Código

O arquivo `modulo3.py` contém:

- Declaração de variáveis no início do programa.
- Cada item implementado de forma individual, separado com comentários `# Item 1`, `# Item 2`, etc.
- Uso de estruturas condicionais para verificar as relações entre `A` e `B`.
- Impressões conforme os resultados de cada teste lógico.

---

## ✅ Conteúdo dos Itens

### Item 1
Verifica se `A > 10`. Se verdadeiro, imprime `"A > 10"`. Em seguida, verifica se `A + B == 20`, imprimindo `"A + B == 20"`. Caso contrário, imprime `"número não válido"`.

### Item 2
Verifica se `A < 10`. Se verdadeiro, imprime `"A < 10"` e também se `A + B == 20`, imprimindo `"A + B == 20"`. Se nenhuma das condições for verdadeira, imprime **apenas** `"número não válido"`.

### Item 3
Verifica três condições: `A == 10`, `A + B == 20` e `B == 10`. Todas as mensagens podem ser exibidas caso sejam verdadeiras.

### Item 4
Verifica se `A > 10` **ou** `A + B == 20`. Se verdadeiro, imprime `"número válido"`. Caso contrário, testa se `A == B`, e se for verdadeiro, imprime `"A é igual B"`. Se ainda não for o caso, verifica se ambos `A` e `B` são diferentes de 10; se não forem, imprime `"número não válido"`.

### Item 5
Verifica se `A > 10`, imprime `"A > 10"` ou `"A <= 10"`. Depois, verifica se `A + B == 20`, imprimindo `"A + B == 20"` ou `"A + B != 20"`.

### Item 6
Verifica se `A > 10` **e** `A + B == 20`. Se verdadeiro, imprime `"A + B == 20"`, senão `"número não válido"`.

### Item 7
Se `A > 10`, imprime `"A > 10"`. Caso contrário, verifica se `A + B == 20`, imprimindo `"A + B == 20"`. Se nenhuma for verdadeira, imprime `"número não válido"`.

### Item 8
Se `A > 10` ou `A + B == 20`, imprime a(s) mensagem(ns) correspondente(s). Se nenhuma for verdadeira, imprime `"números não válidos"`. Independentemente do resultado, sempre imprime: `"Sejam bem-vindos à disciplina de Técnicas de Programação"`.

### Item 9
Verifica se `A > 10` ou `A + B == 20`. Se uma das duas for verdadeira, imprime `"número válido"`. Caso contrário, testa:
- Se `A == B`: imprime `"A é igual B"`.
- Se `A < 10` e ambos `A` e `B` forem diferentes de 10: imprime `"A é menor que 10"`.
- Senão, imprime `"número não válido"`.

### Item 10
Se `A > 10` ou `A + B == 20`, imprime `"números válidos"`, senão `"número não válido"`. Independentemente do resultado, imprime: `"Olá pessoal do BCTec"`.

---

## 🖥️ Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Clone este repositório ou baixe o arquivo `modulo3.py`.
3. Execute o script no terminal:

```bash
python modulo3.py