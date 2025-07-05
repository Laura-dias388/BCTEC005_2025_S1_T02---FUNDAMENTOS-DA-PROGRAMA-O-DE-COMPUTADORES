import random

print("-=" * 50)
print("==" * 50)
print("""1) Paridade: Escreva uma função eh_par(numero) que receba um número e retorne
True se for par e False caso contrário.""")

def eh_par(x):
  return x % 2 == 0

number = random.randint(0, 100)        
eh_par(number)

if eh_par(number):
  print("--" * 50)
  print(f"{number} é Par!!")
else:
  print("--" * 50)
  print(f"{number} não é Par!!")    
print("-=" * 50)

result = eh_par(11) # armazenado o resultado do return dentro da variável result
print("--" * 50)
print(f">>>>>>>>>>>>>>>> {result}")

print("-=" * 50)
print("==" * 50)
print("""2) Saudação: Escreva uma função saudar(nome) que receba um nome como argumento
e imprima uma saudação personalizada. Exemplo: 'Olá, Maria!.'""")

def saudar(nome):
  print("--" * 50)
  print(f"Olá, {nome}!!") # função que imprime uma saudação personalizada, não tem return, apenas printa

saudar("Mundo")

print("-=" * 50)
print("==" * 50)
print("3) Somatório: Sua função deverá receber uma lista e retorna a soma de todos elementos da lista.")

list_number = [1, 2, 3, 4, 5]

def somatorio(lista):
  return sum(lista)

#   soma = 0
#   for numero in lista:
#      soma += numero  # faz o mesmo que a função sum
#   return soma

result = somatorio(list_number)

print("--" * 50)
print(f"A soma do termos da lista é : {result}")

print("-=" * 50)
print("==" * 50)
print("""4) Pesquisa: Sua função deverá receber uma lista e retornar se um dado elemento
está dentro da lista informada. Caso o elemento esteja na lista retornar a posição do
elemento na lista, caso não esteja retornar -100;""")
  
# print("--" * 50)
# minha_lista = [10, 20, 30, 40, 50]
# valor = 30

# print(minha_lista[0])

nomes = ['The Last Of Us', 'GTA 5', 'Dead Space']
for i, v in enumerate(nomes):
  print("--" * 50)
  print(f"indice => {i}, valor => {v}")

def pesquisa(lista, elemento):
  for i, value in enumerate(lista):
    if value == elemento:
      return i
  return -100
print("--" * 50)


lista = [10, 20, 30, 40, 50]
resultado = pesquisa(lista, 30)
print(resultado)

print("--" * 50)

resultado = pesquisa(lista, 99)
print(resultado)

print("--" * 50)

def pesquisa3(lista, elemento):
  if elemento in lista:
    return lista.index(elemento)
  else:
    print("O número não exixte na lista!")
    return -100


resultado = pesquisa3([10, 20, 30, 40], 30)
print(f">> {resultado} <<")  
resultado2 = pesquisa3([10, 20, 30, 40], 99)
print(f">> {resultado2} <<")

print("--" * 50)
print("""Pesquisa por índice: Sua função deverá receber uma lista e retornar o elemento da
lista por meio de um índice informado. Seu programa deverá tratar os casos em que
o índice não existe na lista.""")

# def pesquisa2(lista, elemento):
#   try:
#     return lista.index(elemento)
#   except ValueError:
#     print("O número não exixte na lista!")
#     return -100
  
# number = input("Digite um número: ")
# print(f">> {pesquisa2([10, 20, 30, 40], number)} <<") 

# print(f">> {pesquisa2([10, 20, 30, 40], 90)} <<")

print("--" * 50)
def pesquisa(lista, elemento):
  for i, value in enumerate(lista):
    if value == elemento:
      print(f"O número {elemento} existe na lista no índice {i}.")
      return i
  print(f"O número {elemento} não existe na lista!")
  return -100

print("--" * 50)
try:
  indice = int(input("Digite um número: "))
  lista = [10, 20, 30, 40, 50]
  resultado = pesquisa(lista, indice)
  print(f"Resultado da pesquisa: {resultado}")
except ValueError:
  print("Você deve digitar um número inteiro!")