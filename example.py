import random
print("3) Somatório: Sua função deverá receber uma lsita e retorna a soma de todos elementos da lista.")

def somatorio(lista):
  total = 0
  for numero in lista:
    total += numero
  return total

lista = [1, 2, 3, 4, 5]
resultado = somatorio(lista)

print(f"A soma dos elementos da lista {lista} é: {resultado}")

print("-=" * 50)
print("""4) Verificação de Palíndromo: Sua função deverá receber uma string e retornar True se a string
for um palíndromo (lê-se da mesma forma de trás para frente) e False caso contrário.""")

def eh_palindromo(s):
    s = s.lower().replace(" ", "")  # Normaliza a string
    return s == s[::-1]  # Compara a string com sua reversa
palavra = "arara"
resultado_palindromo = eh_palindromo(palavra)
if resultado_palindromo:
    print(f"{palavra} é um palíndromo!")
else:
    print(f"{palavra} não é um palíndromo!")


print("-=" * 50)
print("""5) Fatorial: Sua função deverá receber um número inteiro e retornar o fatorial do número.
       O fatorial de um número n é o produto de todos os números inteiros de 1 até n.""")

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

numero_fatorial = 5
resultado_fatorial = fatorial(numero_fatorial)

print(f"O fatorial de {numero_fatorial} é: {resultado_fatorial}")

print("-=" * 50)
print("6) Números Primos: Sua função deverá receber um número inteiro e retornar True se o número for primo e False caso contrário.")

def eh_primo(n):                                                    
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
numero_primo = 29
resultado_primo = eh_primo(numero_primo)
if resultado_primo:
    print(f"{numero_primo} é um número primo!")
else:
    print(f"{numero_primo} não é um número primo!")
print("-=" * 50)

print("7) Contagem de Vogais: Sua função deverá receber uma string e retornar o número de vogais presentes na string.")

def contar_vogais(s):
    vogais = "aeiouAEIOU"
    contador = 0
    for char in s:
        if char in vogais:
            contador += 1
    return contador
texto = "Olá, Mundo!"
resultado_vogais = contar_vogais(texto)

print(f"O número de vogais em '{texto}' é: {resultado_vogais}")

print("-=" * 50)
print("8) Conversão de Temperatura: Sua função deverá receber uma temperatura em graus Celsius e retornar a temperatura convertida para Fahrenheit.")

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32     
temperatura_celsius = 25
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C é igual a {temperatura_fahrenheit} °F")

print("-=" * 50)
print("""9) Jogo de Adivinhação: Sua função deverá receber um número aleatório e permitir
que o usuário tente adivinhar o número. A função deve informar se o pal pite está correto, se é maior ou menor que o número aleatório.""")

def jogo_adivinhacao(numero_aleatorio):   
    tentativas = 0
    while True:
        palpite = int(input("Adivinhe o número (entre 1 e 100): "))
        tentativas += 1
        if palpite < numero_aleatorio:
            print("Muito baixo! Tente novamente.")
        elif palpite > numero_aleatorio:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabéns! Você acertou o número {numero_aleatorio} em {tentativas} tentativas.")
            break
numero_aleatorio = random.randint(1, 100)
jogo_adivinhacao(numero_aleatorio)

print("-=" * 50)
print("""10) Calculadora Simples: Sua função deverá receber dois números e uma operação 
(soma, subtração, multiplicação ou divisão) e retornar o resultado da operação.""")
def calculadora(num1, num2, operacao):
    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    elif operacao == 'divisao':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero!"
    else:
        return "Operação inválida!"       
num1 = 10
num2 = 5
operacao = 'soma'
resultado_calculadora = calculadora(num1, num2, operacao)
print(f"O resultado da {operacao} entre {num1} e {num2} é: {resultado_calculadora}")

print("-=" * 50)
print("11) Fibonacci: Sua função deverá receber um número inteiro n e retornar a sequência de Fibonacci até o n-ésimo termo.")

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]
n_termos = 10
resultado_fibonacci = fibonacci(n_termos)
print(f"A sequência de Fibonacci até o {n_termos}-ésimo termo é: {resultado_fibonacci}")

print("-=" * 50)
print("""12) Anagrama: Sua função deverá receber duas strings e retornar True se as strings
forem anagramas (ou seja, se contiverem as mesmas letras em ordens diferentes) e False caso contrário.""")
def sao_anagramas(s1, s2):
    return sorted(s1) == sorted(s2)
string1 = "amor"
string2 = "roma"
resultado_anagrama = sao_anagramas(string1, string2)
if resultado_anagrama:
    print(f"{string1} e {string2} são anagramas!")
else:
    print(f"{string1} e {string2} não são anagramas!")

print("-=" * 50)
print("13) Contagem de Consoantes: Sua função deverá receber uma string e retornar o número de consoantes presentes na string.")
def contar_consoantes(s):
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    contador = 0
    for char in s:
        if char in consoantes:
            contador += 1
    return contador
texto_consoantes = "Olá, Mundo!"
resultado_consoantes = contar_consoantes(texto_consoantes)
print(f"O número de consoantes em '{texto_consoantes}' é: {resultado_consoantes}")

print("-=" * 50)
print("14) Conversão de Temperatura: Sua função deverá receber uma temperatura em graus Fahrenheit e retornar a temperatura convertida para Celsius.")
def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
temperatura_fahrenheit = 77
temperatura_celsius = fahrenheit_para_celsius(temperatura_fahrenheit)
print(f"{temperatura_fahrenheit}°F é igual a {temperatura_celsius} °C")

print("-=" * 50)
print("""15) Jogo de Adivinhação: Sua função deverá receber um número aleatório e permitir
que o usuário tente adivinhar o número. A função deve informar se o palpite está correto, se é maior ou menor que o número aleatório.""")
def jogo_adivinhacao(numero_aleatorio):   
    tentativas = 0
    while True:
        palpite = int(input("Adivinhe o número (entre 1 e 100): "))
        tentativas += 1
        if palpite < numero_aleatorio:
            print("Muito baixo! Tente novamente.")
        elif palpite > numero_aleatorio:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabéns! Você acertou o número {numero_aleatorio} em {tentativas} tentativas.")
            break
numero_aleatorio = random.randint(1, 100)
jogo_adivinhacao(numero_aleatorio)

print("-=" * 50)
print("""16) Calculadora Simples: Sua função deverá receber dois números e uma operação
(soma, subtração, multiplicação ou divisão) e retornar o resultado da operação.""")
def calculadora(num1, num2, operacao):
    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    elif operacao == 'divisao':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero!"
    else:
        return "Operação inválida!"     
num1 = 10
num2 = 5
operacao = 'soma'
resultado_calculadora = calculadora(num1, num2, operacao)
print(f"O resultado da {operacao} entre {num1} e {num2} é: {resultado_calculadora}")

print("-=" * 50)
print("""17) Fatorial: Sua função deverá receber um número inteiro e retornar o fatorial o número.
O fatorial de um número n é o produto de todos os números inteiros de 1 até n.""")
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
numero_fatorial = 5
resultado_fatorial = fatorial(numero_fatorial)
print(f"O fatorial de {numero_fatorial} é: {resultado_fatorial}")
print("-=" * 50)


