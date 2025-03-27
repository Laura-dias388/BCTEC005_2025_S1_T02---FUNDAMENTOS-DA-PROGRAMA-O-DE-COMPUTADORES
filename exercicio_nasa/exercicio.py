print(f"========================================================================================")

# defini o limite de bagagem por tripulante com valor fixo
limite_por_tripulante = 80

nome_comandante=input("Nome do astronauta comandante da missão: ")
distancia= float(input("Distancia da Terra ate Marte (em milhoes de km): ")) # a média é de 225 milhões de quilômetros.
quantidade_de_tripulantes= int(input("Quantidade de tripulantes na nave: "))
consumo_combustivel=float(input("Consumo de combustível por milhão de km (em litros): ")) # 5000 toneladas ≈ 70.422.537litros
custo=float(input("Custo do litro de combustível (em reais): ")) 
refeicao= int(input("Quantidade média de refeições por dia por tripulante: "))
duracao=float(input("Duração estimada da viagem (em dias): ")) # código feito na aula
print(f"========================================================================================")
print(f">>>>>Cada tripulante poderá levar apenas uma mochila e uma mala<<<<<")
print(f"========================================================================================")
volume_mochila = float(input("Volume da sua mochila (em litros): "))
volume_mala = float(input("Volume da mala (em litros): "))

print(f"========================================================================================")

total_combustivel = distancia * consumo_combustivel

custo_total_combustivel = total_combustivel * custo

total_refeicoes = quantidade_de_tripulantes *  refeicao * duracao

volume_total_disponivel = quantidade_de_tripulantes * limite_por_tripulante

volume_utilizado = quantidade_de_tripulantes * (volume_mochila + volume_mala)
  
espaço_restante = volume_total_disponivel - volume_utilizado


print(f"Nome do astronauta comandante da missão: {nome_comandante}")
print(f"Distancia da Terra ate Marte (em milhoes de km): {distancia}")
print(f"Total de combustivel: {total_combustivel}")
print(f"Custo total do combustivel: {custo_total_combustivel}")
print(f"========================================================================================")
print(f"Total refeicoes: {total_refeicoes}")
print(f"O total de tripulantes é: {quantidade_de_tripulantes}")
print(f"O volume total disponível é: {volume_total_disponivel}")
print(f"O volume utilizado foi de: {volume_utilizado}")
print(f"========================================================================================")
print(f"O espaço restante é de: {espaço_restante}")