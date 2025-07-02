print("================================================================")
import random
print("================================================================")
print("Exercício - 01")

lista_cem = []

cont = 0
for i in range(100):
  number = random.randint(-100, 100)
  cont = cont + 1
  lista_cem.append(number)
print(lista_cem)
print(type(lista_cem))

print("----------------------------------------------------------------")
print("a) Imprima os números positivos")

lista_positivos = []

for i in lista_cem:
  if i > 0:
    lista_positivos.append(i)

print(lista_positivos)   

print("----------------------------------------------------------------")
print("b) Imprima os números negativos")

lista_negativos = []

for i in lista_cem:
  if i < 0:
    lista_negativos.append(i)

print(lista_negativos)

print("----------------------------------------------------------------")
print("c) Imprima os números pares")
lista_pares = []

for i in lista_cem:
  if(i % 2 == 0):
    lista_pares.append(i)
print(lista_pares) 

print("----------------------------------------------------------------")
print("d) Imprima os números ímpares")
lista_impares = []

for i in lista_cem:
  if(i % 2 != 0):
    lista_impares.append(i)
print(lista_impares) 

print("----------------------------------------------------------------")
print("e) Imprima os números múltiplos de 4")
lista_multiplos_4 = []

for i in lista_cem:
  if(i % 4 == 0):
    lista_multiplos_4.append(i)
print(lista_multiplos_4) 

print("----------------------------------------------------------------")
print("f) Imprima o maior número da lista")

maior = 0

for i in lista_cem:
  if i > maior:
    maior = i

print(maior)

print("----------------------------------------------------------------")
print("g) Imprima o menor número da lista")

menor = lista_cem[0] #evitar bugs acessando o primeiro elemento e fazendo a verificação

for i in lista_cem:
  if i < menor:
    menor = i

print(menor)

print("----------------------------------------------------------------")
print("h) Imprima a média dos número da lista")

soma = 0

for i in lista_cem:
  soma += i
media = soma / len(lista_cem)

print(f"A soma será de {soma} e a média será {media}")

print("----------------------------------------------------------------")
print("i) Ordene os elementos da lista em ordem crescente")

order = sorted(lista_cem)
print(order)

print("================================================================")
print("Exercício - 02")
 
print("----------------------------------------------------------------")
print("a) Imprima o terceiro elemento da lista")

print(lista_cem[2])

print("----------------------------------------------------------------")
print("b) Acesse o último elemento da lista")

print(lista_cem[-1])

print("----------------------------------------------------------------")
print("c) Modifique o quinto elemento da lista para o número 50")

lista_cem[4] = 50
print(lista_cem)

print("----------------------------------------------------------------")
print("d) Adicione o número 11 ao final da lista")

lista_cem[-1] = 11
print(lista_cem)

print("----------------------------------------------------------------")
print("e) Insira o número 0 no início da lista")

lista_cem[0] = 0
print(lista_cem)

print("----------------------------------------------------------------")
print("f) Remova o último elemento da lista")

lista_cem.pop()
print(lista_cem)

print("----------------------------------------------------------------")
print("g) Remova o elemento 50 da lista")

lista_cem.remove(lista_cem[49])
print(lista_cem)

print("----------------------------------------------------------------")
print("h) Verifique se o número 5 está na lista")

if 5 in lista_cem:
  
  print("O número 5 está na lista!!")

else:
  print("Não tem número 5 nessa lista!")  

print("================================================================")
print("Exercício - 03")
print("Crie uma nova lista que contenha os quadrados dos números de 1 a 10")


print("================================================================")
print("Exercício - 04")
print("Crie uma lista contendo apenas os números pares de 1 a 20")



print("================================================================")
print("Exercício - 05")
print("Crie uma lista com os elementos da lista original multiplicados por 2")