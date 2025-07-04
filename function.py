import random

print("-=" * 50)
print("1) Paridade: Escreva uma função eh_par(numero) que receba um número e retorne True se for par e False caso contrário.")

def eh_par(x):
  return x % 2 == 0

number = random.randint(0, 100)        
eh_par(number)

if eh_par(number):
  print(f"{number} é Par!!")
else:
  print(f"{number} não é Par!!")    
print("-=" * 30)

result = eh_par(11) # armazenado o resultado do return dentro da variável result
print(f">>>>>>>>>>>>>>>>{result}")

print("-=" * 50)
print("2) Saudação: Escreva uma função saudar(nome) que receba um nome como argumento e imprima uma saudação personalizada. Exemplo: 'Olá, Maria!.'")

def saudar(nome):
  print(f"Olá, {nome}!!")

saudar("Mundo")
