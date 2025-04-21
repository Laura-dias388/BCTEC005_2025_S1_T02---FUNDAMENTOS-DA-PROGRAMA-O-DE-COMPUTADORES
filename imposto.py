login = input("Informe seu login: ")
senha = input("Informe sua senha: ")

if((login == "ana" and senha ==  "12345") or (login == "joao" and senha ==  "54321")):
     print ("Você está logado. Seja bem vindo!")
     renda_anual = float(input("Digite sua renda anual (em R$): "))
     tipo_imposto= int(input("Escolha o tipo de imposto 1 para simplificado e 2 para completo: "))
     despesas_medicas = float(input("Digite suas despesas médicas (em R$): "))
     despesas_escolares = float(input("Digite suas despesas escolares (em R$): "))
     despesas_livros = float(input("Digite suas despesas com livros (em R$): "))
     despesas_viagens = float(input("Digite suas despesas com viagens (em R$): "))
    
    # imposto=0


     if(renda_anual <=  22847.76):
          imposto=0
     elif(renda_anual <= 33919.80 ):
          imposto = renda_anual * 0.075
     elif (renda_anual <= 45012.60):
        imposto = renda_anual * 0.15
     elif (renda_anual <=  55976.16):
        imposto = renda_anual * 0.225
     else:
        imposto = renda_anual * 0.275

     
     print("valor imposto: ", imposto)

else:
     print("Você não está logado. A senha ou login estão erradas")