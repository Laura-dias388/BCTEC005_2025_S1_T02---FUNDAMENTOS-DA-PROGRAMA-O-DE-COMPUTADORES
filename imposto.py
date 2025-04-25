print("================================================================================================")

login = input("Informe seu login: ")
senha = input("Informe sua senha: ")


if (login == "ana" and senha == "12345") or (login == "joao" and senha == "54321"):
    print("Você está logado. Seja bem vindo!")

    renda_anual = float(input("Digite sua renda anual (em R$): "))
    tipo_imposto = int(input("Escolha o tipo de imposto >>1<< para simplificado e >>2<< para completo: "))
    despesas_medicas = float(input("Digite suas despesas médicas (em R$): "))
    despesas_escolares = float(input("Digite suas despesas escolares (em R$): "))
    despesas_livros = float(input("Digite suas despesas com livros (em R$): "))
    despesas_viagens = float(input("Digite suas despesas com viagens (em R$): "))
    DESPESAS = ((despesas_medicas * 0.05) + (despesas_escolares * 0.10) + (despesas_livros * 0.02) + (despesas_viagens * 0.30))

    if tipo_imposto == 1 and renda_anual <= 45012.60:
        imposto = 0
        imposto_real = renda_anual * 0.09
        imposto = imposto_real - DESPESAS
        print(f"O valor do seu imposto após as deduções será de: { imposto:.2f}")
    else:    

    # imposto=0
      if renda_anual <= 22847.76:
          imposto = 0
          
      elif renda_anual <= 33919.80:
          imposto_22 = renda_anual - 22847.76
          imposto_real = imposto_22 * 0.075

      elif renda_anual <= 45012.60:
          imposto_33 = renda_anual - 33919.80
          imposto_22 = 33919.80 - 22847.76
          imposto_real = (imposto_22 * 0.075) + (imposto_33 * 0.15)

      elif renda_anual <= 55976.16:
          imposto_45 = renda_anual - 45012.60
          imposto_33 = 45012.60 - 33919.80
          imposto_22 = 33919.80 - 22847.76
          imposto_real = (imposto_22 * 0.075) + (imposto_33 * 0.15) + (imposto_45 * 0.225)
      else:
          imposto_55 = renda_anual - 55976.16
          imposto_45 = 55976.16 - 45012.60
          imposto_33 = 45012.60 - 33919.80
          imposto_22 = 33919.80 - 22847.76
          imposto_real = (imposto_22 * 0.075) + (imposto_33 * 0.15) + (imposto_45 * 0.225) + (imposto_55 * 0.275)

      imposto = imposto_real - DESPESAS
      print(f"O valor do seu imposto após as deduções será de: { imposto:.2f}")

else:
    print("Você não está logado. A senha ou login estão erradas")
