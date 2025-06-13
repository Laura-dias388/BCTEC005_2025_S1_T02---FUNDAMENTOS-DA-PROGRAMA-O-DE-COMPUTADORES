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
print("b) Imprima os números negaivos")

lista_negativos = []

for i in lista_cem:
  if i < 0:
    lista_negativos.append(i)

print(lista_negativos) 
print("----------------------------------------------------------------")
print("c) Imprima os números pares")
print("----------------------------------------------------------------")
print("d) Imprima os números ímpares")
print("----------------------------------------------------------------")
print("e) Imprima os números múltiplos de 4")
print("----------------------------------------------------------------")
print("f) Imprima o maior número da lista")
print("----------------------------------------------------------------")
print("g) Imprima o menor número da lista")
print("----------------------------------------------------------------")
print("h) Imprima a média dos número da lista")
print("----------------------------------------------------------------")
print("i) Ordene os elementos da lista em ordem crescente")


print("================================================================")
print("Exercício - 02")
 
print("----------------------------------------------------------------")
print("a) Imprima o terceiro elemento da lista")
print("----------------------------------------------------------------")
print("b) Acesse o último elemento da lista")
print("----------------------------------------------------------------")
print("c) Modifique o quinto elemento da lista para o número 50")
print("----------------------------------------------------------------")
print("d) Adicione o número 11 ao final da lista")
print("----------------------------------------------------------------")
print("e) Insira o número 0 no início da lista")
print("----------------------------------------------------------------")
print("f) Remova o último elemento da lista")
print("----------------------------------------------------------------")
print("g) Remova o elemento 50 da lista")
print("----------------------------------------------------------------")
print("h) Verifique se o número 5 está na lista")
print("================================================================")
print("Exercício - 03")
print("Crie uma nova lista que contenha os quadrados dos números de 1 a 10")


print("================================================================")
print("Exercício - 04")
print("Crie uma lista contendo apenas os números pares de 1 a 20")



print("================================================================")
print("Exercício - 05")
print("Crie uma lista com os elementos da lista original multiplicados por 2")