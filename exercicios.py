# 1: Restrições dos dados de entrada

# qualificacao	Deve ser múltiplo de 4 e entre 1 e 100
qualificacao = int(input(f"Qual o valor de qualificação do seu personagem: "))

if (qualificacao % 4 == 0) and (qualificacao < 100):
  print(f"Alex jovem padawan você esta qualificado")
else:
  print(f"Personagem não quallificado")  

print(f"=============================================================================")

# energia	Entre 0 e 100, e deve ser ≥ (30 + qualificacao × 0.6)
print(f"Seu nível de energia é: ")

energia = int(qualificacao * 0.6)

if energia >= 30:
  print(f"Alex padawan seu nível de energia é: {energia} e está dentro do esperado!")
else:
  print(f"Seu nível de energia esta baixo, tente novamente!!")  

print(f"=============================================================================")

# tem_chave_mestra	Booleano: 'sim' ou 'não' (convertido para True ou False)
choise = str(input(f"Você está em posse da Chave Mestra (Sim/Não): "))

if (choise == "Sim"):
   tem_chave_mestra = True
   print(type(tem_chave_mestra))
   print(f"Uall Você pode seguir seu caminho pelos templo dos códigos fragmentados!!")
else:
  print(f"Lamento sem a chave mestra você não tera chance!")

print(f"=============================================================================")

# localizacao	Deve ser uma entre: 'floresta', 'caverna' ou 'torre'
print("Escolha um caminho: floresta, caverna ou torre: ")

print(f"Para onde você vai: ")
localizacao = str(input("obs: digite o nome em fonte minúscula: "))

if(localizacao == "floresta"):
    print("Você esta nas florestas da Lua de Endor, aproveite!!")
elif(localizacao == "caverna"):
    print("Você esta no planeta Dagobah, cuidado!!")
elif(localizacao == "torre"):
    print("Você esta no planeta-cidade Coruscant!")    
else:
    print("Opção não valida! Tente novamente.") 

print(f"=============================================================================")

# mapa_templo	Deve ser um número inteiro par
mapa_templo = int(input("Digite o número do Mapa do Templo (deve ser um número par): "))

if mapa_templo % 2 == 0:
    print(f"O mapa {mapa_templo} é válido. Continue jovem Padawan.")
    tem_mapa = True
else:
    print("Mapa inválido! Padawan não encontrará todos os segredos.")
    tem_mapa = False

print(f"=============================================================================")

# confiabilidade_sistema	Começa em 50, depois ajusta: + 0.4 × qualificacao, -10 se floresta
confiabilidade = 50
confiabilidade = confiabilidade + (0.4 * qualificacao)

if localizacao == "floresta":
    confiabilidade = confiabilidade - 10

if localizacao == "caverna":
    confiabilidade = confiabilidade - 10

print(f"Sua confiabilidade atual é: {confiabilidade}")

print(f"=============================================================================")

# inteligencia_minima	40 + (0.3 × qualificacao) + (0.2 × energia) - (0.1 × confiabilidade) [+10 se não tiver o mapa]
inteligencia_minima = 40 + (0.3 * qualificacao) + (0.2 * energia) - (0.1 * confiabilidade)

if not tem_mapa:
    inteligencia_minima = inteligencia_minima + 10

print(f"A inteligência mínima exigida para continuar é: {inteligencia_minima}")