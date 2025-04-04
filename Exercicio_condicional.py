#exemplo introdutório: if else
numero = 100

if(numero == 10):
    print("dentro do if")
    print("olá sou um if")
else:
    print("dentro do else")
    print("olá sou o else")


# Fase 1 do jogo
escolha = input("Você quer entrar na Câmara das escolhas, sim  ou não?")
print(escolha)

if(escolha =="sim"):
       print("borá lá!")
else:
    print("volte para fase das variáveis!")


# Exemplo introdutório: elif

numero = int(input("informe o número do portão:"))
nome = "pedro"

if(numero == 3):
    print("Portão de bronze aberto!")
    if(nome == "pedro"):
        print("nome correto")
    else:
        print("nome incorreto")
elif (numero == 5):
    print("Portão de prata aberto!")
elif(numero== 7):
    print("Portão de ouro aberto!")
else:
    print("Número incorreto de chaves. Portão permanece fechado.")
print("Ola tutoria já vai acabar!")