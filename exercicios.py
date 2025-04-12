# 1: Restrições dos dados de entrada

number = int(input(f"Qual o valor de qualificação do seu personagem: "))

if (number % 4 == 0) and (number < 100):
  print(f"Alex você esta qualificado")
else:
  print(f"Personagem não quallificado")  

print(f"Seu nível de energia é: ")

print(f"=============================================================================")

energy = int(number * 0.6)

if energy >= 30:
  print(f"Alex seu nível de energia é : {energy} e está dentro do esperado!")
else:
  print(f"Seu nível de energia esta baixo, tente novamente!!")  

print(f"=============================================================================")

choise = str(input(f"Você está em posse da Chave Mestra (Sim/Não): "))

if choise == "Sim":
   key_master = True
   print(type(key_master))
  
   if key_master == True:
      print(f"Uall Você pode seguir seu caminho pelos templo dos códigos fragmentados!!")
else:
  print(f"Lamento sem a chave mestra você não tera chance!")  


# number = int(input(f"Qual o valor de qualificação do seu personagem: "))
# if (number % 4 == 0) and (number <100):
#   print(f"Alex você esta qualificado")

# number = int(input(f"Qual o valor de qualificação do seu personagem: "))

# if (number % 4 == 0) and (number <100):
#   print(f"Alex você esta qualificado")

# number = int(input(f"Qual o valor de qualificação do seu personagem: "))

# if (number % 4 == 0) and (number <100):
#   print(f"Alex você esta qualificado")
