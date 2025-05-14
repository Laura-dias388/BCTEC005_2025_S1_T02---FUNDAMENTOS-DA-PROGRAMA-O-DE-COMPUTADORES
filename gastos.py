import pandas as pd
#import matplotlib.pyplot as plt

df = pd.read_csv("gastos.csv")

print("==============================================================================================")
print("Exercício 1")

for indice, conteudo_linha in df.iterrows():
    if(conteudo_linha["valor"]> 1000):
      print(f" Alerta, responsável: {conteudo_linha['responsável']} gastou: {conteudo_linha['valor']} ")

print("==============================================================================================")
print("Exercício 2")

cursos = 0
for indice, conteudo_linha in df.iterrows():
    if(conteudo_linha["categoria"].lower() == "cursos"):
      cursos = cursos + conteudo_linha["valor"]
print(f"Valores gastos com cursos total foi:>> {cursos: .2f}")

print("==============================================================================================")
print("Exercício 3")

total_transporte = 0
for indice, conteudo_linha in df.iterrows():
    if(conteudo_linha["categoria"].lower() == "transporte"):
       total_transporte = total_transporte + conteudo_linha["valor"]
print(f"Valor total gasto com transporte foi:>> {total_transporte: .2f} ")

print("==============================================================================================")
print("Exercício 4")

soma_gastos_ana = 0
for indice, conteudo_linha in df.iterrows():
    if(conteudo_linha["responsável"].lower() == "ana"):
       soma_gastos_ana = soma_gastos_ana + conteudo_linha["valor"]
print(f"Valor total de gastos da Ana foi:>> {soma_gastos_ana: .2f} ")

print("==============================================================================================")
print("Exercício 5")

soma_gastos = 0
for indice, conteudo_linha in df.iterrows():
    if(conteudo_linha["categoria"].lower() == "alimentação", "hospedagem", "transporte"): # refatorar
       soma_gastos = soma_gastos + conteudo_linha["valor"]
print(f"Valor total de gastos com alimentação, hospedagem e transporte foi:>> {soma_gastos: .2f} ")

print("==============================================================================================")
print("Exercício 6")

for indice, conteudo_linha in df.iterrows():
   if(conteudo_linha["data"] == "2023-02-01"):
        print(
            f"Os registros existentes na data 2023-02-01 são:\n"
            f"Categoria: {conteudo_linha['categoria']},\n"
            f"Valor: {conteudo_linha['valor']},\n"
            f"Responsável: {conteudo_linha['responsável']}"
        )

print("==============================================================================================")
print("Exercício 7")

for indice, conteudo_linha in df.iterrows():
   
    maior_gasto = 0
    if(conteudo_linha["valor"] > maior_gasto):
      maior_gasto += conteudo_linha["valor"]
print(f"O maior gasto registrado foi: {maior_gasto: .2f}")

print("==============================================================================================")
print("Exercício 8")
print("==============================================================================================")
print("Exercício 9")
print("==============================================================================================")
print("Exercício 10")



