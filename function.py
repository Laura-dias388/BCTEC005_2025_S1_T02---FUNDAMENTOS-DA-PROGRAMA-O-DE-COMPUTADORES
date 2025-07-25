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
print("""5) Pesquisa por índice: Sua função deverá receber uma lista e retornar o elemento da
lista por meio de um índice informado. Seu programa deverá tratar os casos em que
o índice não existe na lista.""")

def pesquisa_por_indice(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        print(f"Índice {indice} não existe na lista!")
        return None

lista = [10, 20, 30, 40, 50]

try:
    indice = int(input("Digite um índice: "))
    resultado = pesquisa_por_indice(lista, indice)
    if resultado is not None:
        print(f"Elemento no índice {indice}: {resultado}")
except ValueError:
    print("Você deve digitar um número inteiro!")

print("--" * 50)
print("""6) Separação de valores positivos e valores negativos: Sua função deverá receber
uma lista e deverá organizar os elementos nessa lista de forma que os números
negativos fiquem nas primeiras posições e os números positivos fiquem na últimas
posições.""")

def valuables_organizer(value):
  list_numbers_positive = []
  list_numbers_negative = []
  for i in value:
    if i > 0:
      list_numbers_positive.append(i)
    else:
      list_numbers_negative.append(i)

  mega_list = list_numbers_negative + list_numbers_positive
  mega_list.sort()
  print(mega_list)

numbers = [-2, 1, 0, -8, -100, 80, 20, -12, -18, 28]
valuables_organizer(numbers)

print("--" * 50)
print("""7) Número aleatórios: Faça uma função que retorne uma lista com 100 números
aleatórios.""")

def numbers_aleatorys():
  list_numbers = []
  for _ in range(100):
    number = random.randint(-100, 100)
    list_numbers.append(number)
  print(list_numbers)

numbers_aleatorys()
print("--" * 50)
