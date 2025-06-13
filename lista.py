print("===============================================================================")

print("Fase 1 - O Cofre dos Tesouros Escondidos")

tesouros = ["anel", "moeda", "esmeralda", "espelho", "poção", "mapa"]

print("-------------------------------------------------------------------------------")
print("1.1")
print(tesouros[2]) #esmeralda

print("-------------------------------------------------------------------------------")
print("1.2")
tesouros[4] = "graal" 
print(tesouros[4])

print("-------------------------------------------------------------------------------")
print("1.3")
print(tesouros)# ['anel', 'moeda', 'esmeralda', 'espelho', 'graal', 'mapa']

print("-------------------------------------------------------------------------------")
print("1.4")

for i in range(len(tesouros)):

  print(f"Para o índice: {i} o valor é: {tesouros[i]}")

print("===============================================================================")

print("Fase 2 - O Caminho da Soma Oculta")

valores = [7, 3, 10, 2, 8, 5]

print("-------------------------------------------------------------------------------")
print("2.1")

soma = 0

for i in range(len(valores)):
  print(f"{soma} + {valores[i]} = {soma + valores[i]}")
  soma += valores[i]

print("-------------------------------------------------------------------------------")
print("2.2")
print(f"A soma será: {soma}")

print("===============================================================================")
print("Fase 3 - O Desafio do Espelho Partilhado")

equipamentos = ["escudo", "capacete", "capa", "luvas", "botas"]

print("-------------------------------------------------------------------------------")
print("3.1")

equipamentos[0] = "botas"
equipamentos[-1] = "escudo"

print(equipamentos) # ['botas', 'capacete', 'capa', 'luvas', 'escudo']

print("-------------------------------------------------------------------------------")
print("3.2")

equipamentos[1] = "luvas"
equipamentos[3] = "capacete"

print("-------------------------------------------------------------------------------")
print("3.3")

print(equipamentos) # ['botas', 'luvas', 'capa', 'capacete', 'escudo']

print("===============================================================================")
print("Fase 4 - Balanço das Pedras Preciosas")

stones = []

stones = stones + ["diamante"]
print(stones)

stones = stones + ["safira"]
print(stones)

stones = stones + ["jade", "rubi", "esmeralda"]
print(stones)

print("===============================================================================")
print("Fase 5 - O Labirinto da Busca Secreta")

runa_ordenada = [2, 5, 9, 12, 15, 18, 21, 24, 27, 30]

choise_number = int(input("Escolha um número para ver se é o número mágico >> DICA: entre 1 e 50 <<: "))

if choise_number in runa_ordenada:
  print(f"Você encontrou o número mágico!! >> |{choise_number}| <<")
else:
  print(f"Continue tentando o número >> |{choise_number}| << não é o número mágico!!")  

print("===============================================================================")
print("Fase 6 - A União dos Reinos Fragmentados")

reliquias_a = [3, 7, 12, 20, 25] 
reliquias_b = [4, 6, 15, 22, 30, 35]

fusion_list = reliquias_a + reliquias_b
    
fusion_list.sort()
print(fusion_list)

print("===============================================================================")
print("Fase 7 - Contagem das pedras")

pedras = ["jade", "rubi", "jade", "esmeralda", "rubi", "ágata", "jade", "ágata","jade", 
"rubi", "jade", "esmeralda", "rubi", "ágata", "jade", "ágata","jade", 
"rubi","esmeralda", "rubi"]

print("-------------------------------------------------------------------------------")
new_list  = []
for stone in set(pedras): # Iteramos apenas sobre os elementos únicos da lista
  if pedras.count(stone) > 1: # Se o elemento aparece mais de uma vez, ele é repetido
    new_list.append(stone)
print(f"Os itens repetidos são: {new_list}")

print("===============================================================================")
print("Fase 8 - Os Desafios Básicos de Alex")
fragmentos = [4, 7, 1, 8, 5, 2, 9, 3, 6]

print("-------------------------------------------------------------------------------")
print("8.1")

fragmentos[0] = 6
fragmentos[-1] = 4
print(fragmentos)

print("-------------------------------------------------------------------------------")
print("8.2")
soma = 0
for piece in range(len(fragmentos)):
  soma += fragmentos[piece]
print(f"A soma de todos os valores será: {soma}")

print("-------------------------------------------------------------------------------")
print("8.3")

even_number = 0

for i in fragmentos:
  if(i % 2 == 0):
    even_number += 1
print(f"Existem {even_number} números pares!")

print("-------------------------------------------------------------------------------")
print("8.4")

for i in range(len(fragmentos)):
    if fragmentos[i] % 2 != 0:
        fragmentos[i] = 0
print(fragmentos)

print("-------------------------------------------------------------------------------")
print("8.5")

fragmentos2 = [4, 7, 1, 8, 5, 2, 9, 3, 6]
print(fragmentos2)

average = 0
counter = 0
total = 0

for piece in range(len(fragmentos2)):
  total += fragmentos2[piece]
  counter += 1
  average = total / counter

print(f"A média obtida a partir da soma de todos os valores é: {average:.0f}")

print("-------------------------------------------------------------------------------")
print("8.6")

fragmentos2 = [4, 7, 1, 8, 5, 2, 9, 3, 6]
print(fragmentos2)

multiplication = []
# counter = 0
element = 0

for piece in range(len(fragmentos2)):
  
  multiplication.append(fragmentos2[piece] * 2)
  # counter += 1
print(multiplication)

print("-------------------------------------------------------------------------------")
print("8.7")

big = max(fragmentos2)
print(f"O maior elemento calculado com a função max é: {big}")

small = min(fragmentos2)
print(f"O menor elemento calculado com a função min é: {small}")

maior = 0
menor = 2

for piece in range(len(fragmentos2)):
  if(fragmentos2[piece] > maior):
    maior = fragmentos2[piece]
   
  elif(fragmentos2[piece] < menor):
    menor = fragmentos2[piece]  
    
print(f"O maior elemento calculado apenas com lógica é: {maior}")
print(f"O menor elemento calculado apenas com lógica é: {menor}")