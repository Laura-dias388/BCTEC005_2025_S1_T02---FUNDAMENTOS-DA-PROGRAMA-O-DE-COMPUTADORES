print("=======================================================================================")
print("Exercício 1")
# Exercício 1 - O Portal das Perguntas

pergunta = input("Você deseja continuar a jornada? (sim/não):  ")

while(pergunta != "sim"):
    print("Resposta inválida para avançar. Tente novamente!")
    pergunta = input("Você deseja continuar a jornada? (sim/não): ")

print("fim do programa!")

print("=======================================================================================")
print("Exercício 2")
# Exercício 2 - A Subida da Escada Infinita

degrau_limite = int(input("informe o degrau limite: "))
degrau_aleatorio = int(input("informe o degrau aleatorio: "))

degrau = 1 
while(degrau <= degrau_limite):
    
    if(degrau == degrau_aleatorio):
        print("Estou no degrau: ", degrau)

    if(degrau == degrau_limite):
        print("Você chegou ao topo da escada! degrau: ", degrau_limite)
    
    degrau += 1

print("=======================================================================================")
print("Exercício 3")
# Exercício 3 - A Contagem das Pedras Luminosas

total_pedras = 0
for numero in range(1,3):
    print("ponto de coleta", numero)

    pedras = int(input("Informe a quantidade de pedras coletadas? "))
    print(f"Ponto de coleta: {numero} - número de pedras coletadas: {pedras}!")

    total_pedras = total_pedras + pedras

print("Número de pedreas coletadas foi: ", total_pedras )

print("=======================================================================================")
print("Exercício 4")
# Exercício 4: Escolha do Caminho no Labirinto

x = 1
while(x <= 5):
    y = 1
    while(y <= 10):
        print( x , " * ", y , " = ", x * y)
        y += 1
    
    print("===============")
    x += 1
print("Seu caminho está liberado!")
    
print("=======================================================================================")
print("Exercício 5")
# Exercício 5: Cofre Codificado com Adivinhação

import random

# random - número entre 1 e 10
key = int(input("Digite o número da chave (entre 1 e 10): "))

for x in range(11): 
    numero_aleatorio = random.randint(1, 10)
    # print(numero_aleatorio)
    if(numero_aleatorio == key):
        senha = int(input("Digite o código de segurança: "))
        if(senha == 8):
           print(f"Cofre aberto com sucesso! Tesouro liberado! Você acertou a chave: {key} e o código de segurança: {senha}")

# if(numero_aleatorio != key):        
#     print("Você não acertou a chave secreta!")           

print("=======================================================================================")
print("Exercício 6")
# Exercício 6: O Enigma dos Dois Caminhos

numberX = 100

while(numberX > 1):
    numberX = numberX - 1
    numberY = 1
    while(numberY < 100):
        numberY = numberY + 1
        # print(numberX, numberY)
        cont = numberX + (2 * numberY)
        
        if(cont == 150):
           print(f"Equilíbrio encontrado em x = {numberX}, y = {numberY} = 150")


print("=======================================================================================")
print("Exercício 7")
# Exercício 7: O Portal dos Dois Guardiões


# - x de 100 até 1
# - y de 1 até 100
# - Condições:
# - abs(x - y) < 5
# - x * y > 3000
#   > `Quando ambas forem verdadeiras, abra o portal.
x = 100

while(x > 1):
    y = 1
    # print(x)
    while(y < 100):
    #    print(y)
       y += 1
    x -= 1
    cont_one = abs(x - y) < 5
    cont_two = (x * y) > 3000
    
    print(cont_one, "|", cont_two)
    if(cont_one == True and cont_two == True):
      print("Portal aberto!!")

print("fim!")

print("=======================================================================================")
print("Exercício 8")
# Exercício 8: O Santuário das Constelações

energy = 100

point_gema = 2

constellation = 11

while constellation > 0:
    constellation -= 1
    gema = int(input(f"Quantas gemas você coletou na {constellation}° constelação? "))
    
    force = (energy - (gema * point_gema))
    energy = force

    print(f"Coletou 5 gemas! Sua energia está em: {energy}")

    if(energy <= 0):
        print("Alex não pode mais coletar!!")
        constellation = 0
    

print("=======================================================================================")
print("Exercício 9")
# Exercício 9:  A Batalha contra o Guardião dos Códigos

import random

strength = 100

guardian = 3 * 50

strength_points = 5

attack_points = 10

attack_failure = 0.3

fight = input("Atacar? sim ou não: ")
if fight == "sim":

  for x in range(11): 
    attack_aleatorio = random.randint(1, 100)
    injured_target = attack_aleatorio * attack_failure
    if(injured_target):
      guardian -= 10
      print(f"O Guardião perdeu {guardian} pontos de proteção!")
    else:  
      strength -= 5
      if guardian <= 0:
            print("Camada Destruída! Alex venceu!!!!!!!")
      if strength <= 0:
            print("Alex pedeu!")   