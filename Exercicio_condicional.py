print("Cofre Codificado com Adivinhação 😎")
#exemplo introdutório: if else

print("=================================================================================")
numero = 100

if(numero == 10):
    print("dentro do if")
    print("olá sou um if")
else:
    print("dentro do else")
    print("olá sou o else")
print("=================================================================================")

# Fase 1 do jogo
escolha = input("Você quer entrar na Câmara das escolhas, sim  ou não? 🤔: ")
print(escolha)

if(escolha =="sim"):
       print("borá lá! 🏃‍♂️‍➡️")
else:
    print("volte para fase das variáveis!")

print("=================================================================================")
# Exemplo introdutório: elif

numero = int(input("informe o número do portão: "))
nome = str(input("Qual seu nome: "))

if(numero == 3):
    print("Portão de bronze aberto!")
    if(nome == "Laura"):
        print("nome correto")
    else:
        print("nome incorreto")
elif (numero == 5):
    print("Portão de prata aberto!")
elif(numero == 7):
    print("Portão de ouro aberto!")
else:
    print("Número incorreto de chaves. Portão permanece fechado.")

print("=================================================================================")
# print("Ola tutoria já vai acabar!")
# Fase 3

print(" Verificação do nível de força do personagem")
forca = int(input("Qual o nível de força do seu personagem? "))

if(forca > 100):
    print("Níveis aceitáveis de força")
else:
    print("Precisa estudar mais para melhorar seus níveis de força")    
print("=================================================================================")
# Fase 4: Escolha do Caminho no Labirinto

print("Escolha do Caminho no Labirinto")
print("Escolha um caminho: floresta, caverna ou rio: ")

caminho = str(input("obs: digite o nome em fonte minúscula: "))

if(caminho == "floresta"):
    print("Você foi atacado por robôs-programadores. Volte ao início")
elif(caminho == "caverna"):
    print("Você encontrou um enigma lógico!")
elif(caminho == "rio"):
    print("Você atravessou com sucesso para a próxima fase!")    
else:
    print("Caminho inválido. Tente novamente.")        

print("=================================================================================")

# Fase 5: Cofre Codificado com Adivinhação


senha_secreta = 8


senha_tentativa = int(input("Tente adivinhar a senha entre 1 e 10 🤠: "))

if(senha_secreta == senha_tentativa):
    print("Senha correta! Cofre aberto!")
elif(senha_tentativa < senha_secreta):
    print("Senha muito baixa!")
else:
    # (senha_aecreta > senha_tentativa):
    print(" Senha muito alta!")    

    # print("Senha secreta inválida. Tente novamente.")

print("=================================================================================")

# Fase 6: Termômetro de Temperatura Digital
print("Fase 6: Termômetro de Temperatura Digital")

temperatura = int(input("Digite a temperatura atual 🔥🌡️❄️: "))

if(temperatura > 25):
    print("Muito quente! Robô superaquecido!")    
elif(temperatura < 15):
    print("Muito frio! Robô congelado!")
else:
    print("Temperatura ideal. Robô funcionando!")