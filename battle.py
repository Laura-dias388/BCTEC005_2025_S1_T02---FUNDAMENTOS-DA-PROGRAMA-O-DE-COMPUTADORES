print("=======================================================================================")

# Exercício 1 - O Portal das Perguntas

pergunta= input("Você deseja continuar a jornada? (sim/não):  ")

while(pergunta != "sim"):
    print("Resposta inválida para avançar. Tente novamente!")
    pergunta= input("Você deseja continuar a jornada? (sim/não):  ")
print("fim do programa!")

print("=======================================================================================")

# Exercício 2 - A Subida da Escada Infinita

degrau_limite= int(input("informe o degrau limite: "))
degrau_aleatorio= int(input("informe o degrau aleatorio: "))

degrau = 1 
while( degrau <= degrau_limite):
    
    if(degrau == degrau_aleatorio):
        print("Estou no degrau: ", degrau)

    if(degrau == degrau_limite):
        print("Você chegou ao topo da escada! degrau: ", degrau_limite)
    
    degrau += 1

print("=======================================================================================")

# Exercício 3 - A Contagem das Pedras Luminosas
total_pedras = 0
for numero in range(1,3):
    print("ponto de coleta", numero)

    pedras= int(input("Informe a quantidade de pedras coletadas?"))
    print(f"Ponto de coleta: {numero}  - número de pedras coletadas: {pedras}!")
    total_pedras = total_pedras + pedras
    

print("numero de pedreas coletadas foram: ", total_pedras )

print("=======================================================================================")

x = 1
while(x <= 10):
    y = 1
    while(y <= 10):
        print( x , " * ", y , " = ", x * y)
        y += 1
    
    x += 1
    print(x ,y)
    
print("=======================================================================================")
import random
# random - número entre 1 e 10

for x in range(11): 
    numero_aleatorio = random.randint(1, 10)
    print(numero_aleatorio)

print("=======================================================================================")

# incialização
# condição de parada
# incremento 

repeticao = 1 
quantidade_usuario= int(input("informe a quantidade de usuarios: "))


while(repeticao <= quantidade_usuario):
    print(" senha do cliente")
    senha = input(f"informe seu senha do usuario {repeticao} ")

    if(senha == "123"):
        print("logado")
    else:
        print ("nao logado")
    repeticao += 1

print("fim!")