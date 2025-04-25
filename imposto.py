print("================================================================================================")

login = input("Informe seu login: ")
senha = input("Informe sua senha: ")

ALIQUOTA_075 = 22847.76
ALIQUOTA_15 = 33919.80
ALIQUOTA_225 = 45012.60
ALIQUOTA_275 = 55976.16

if (login == "ana" and senha == "12345") or (login == "joao" and senha == "54321"):
    print("Você está logado. Seja bem vindo!")

    renda_anual = float(input("Digite sua renda anual (em R$): "))
    tipo_imposto = int(input("Escolha o tipo de imposto >>1<< para simplificado e >>2<< para completo: "))
    if tipo_imposto == 1:
        imposto = 0
        imposto = renda_anual * 0.09
        print("Seu imposto será de: ", imposto)
    else:    
      despesas_medicas = float(input("Digite suas despesas médicas (em R$): "))
      despesas_escolares = float(input("Digite suas despesas escolares (em R$): "))
      despesas_livros = float(input("Digite suas despesas com livros (em R$): "))
      despesas_viagens = float(input("Digite suas despesas com viagens (em R$): "))

    # imposto=0
      if renda_anual <= ALIQUOTA_075:
          imposto = 0
          
      elif renda_anual <= ALIQUOTA_15:
          imposto_22 = renda_anual - ALIQUOTA_075
          imposto_real = imposto_22 * 0.075

      elif renda_anual <= ALIQUOTA_225:
          imposto_33 = renda_anual - ALIQUOTA_15
          imposto_22 = ALIQUOTA_15 - ALIQUOTA_075
          imposto_real = (imposto_22 * 0.075) + (imposto_33 * 0.15)

      elif renda_anual <= ALIQUOTA_275:
          imposto_45 = renda_anual - ALIQUOTA_225
          imposto_33 = ALIQUOTA_225 - ALIQUOTA_15
          imposto_22 = ALIQUOTA_15 - ALIQUOTA_075
          imposto_real = (imposto_22 * 0.075) + (imposto_33 * 0.15) + (imposto_45 * 0.225)
      else:
          imposto_55 = renda_anual - ALIQUOTA_275
          imposto_45 = ALIQUOTA_275 - ALIQUOTA_225
          imposto_33 = ALIQUOTA_225 - ALIQUOTA_15
          imposto_22 = ALIQUOTA_15 - ALIQUOTA_075
          imposto_real = (imposto_22 * 0.075) + (imposto_33 * 0.15) + (imposto_45 * 0.225) + (imposto_55 * 0.275)

      imposto = imposto_real - ((despesas_medicas * 0.05) + (despesas_escolares * 0.10) + (despesas_livros * 0.02) + (despesas_viagens * 0.30))
      print(f"O valor do seu imposto será de: { imposto:.2f}")

else:
    print("Você não está logado. A senha ou login estão erradas")
