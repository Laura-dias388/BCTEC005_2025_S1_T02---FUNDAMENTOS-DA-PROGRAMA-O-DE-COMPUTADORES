import pandas as pd
#import matplotlib.pyplot as plt

df = pd.read_csv("gastos.csv")

print("==============================================================================================")
print("Exercício 1")

for indice, conteudo_linha in df.iterrows():
    if(conteudo_linha["valor"]> 1000):
        print(f"Alerta, responsável: {conteudo_linha['responsável']} gastou: {conteudo_linha['valor']} ")

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
        if(conteudo_linha["valor"] > 1000):
            total_transporte = total_transporte + conteudo_linha["valor"]
            print(f"Os valores gastos com transporte acima de mil reais são: {conteudo_linha['valor']}")
print(f"O total gasto com transporte foi:>> {total_transporte: .2f}")

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
media = 0
for indice, conteudo_linha in df.iterrows():
    if(conteudo_linha["categoria"].lower() == "alimentação"): # refatorar
        soma_gastos = soma_gastos + conteudo_linha["valor"]
        media += 1
    if(conteudo_linha["categoria"].lower() == "hospedagem"):
        soma_gastos = soma_gastos + conteudo_linha["valor"]
        media += 1
    if(conteudo_linha["categoria"].lower() == "transporte"):
        soma_gastos = soma_gastos + conteudo_linha["valor"]
        media += 1
# media = soma_gastos / 3           
print(f"A média do valor total de gastos com alimentação, hospedagem e transporte foi:>> {soma_gastos / media: .2f} ")

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

maior_gasto = 0
for indice, conteudo_linha in df.iterrows():
    if(conteudo_linha["valor"] > maior_gasto):
        maior_gasto = conteudo_linha["valor"]
        categoria = conteudo_linha["categoria"]
        responsavel = conteudo_linha["responsável"]
print(f"O maior gasto registrado foi: {maior_gasto: .2f} a categoria é {categoria} e o/a responsável é: {responsavel}")

print("==============================================================================================")
print("Exercício 8")

cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0
cont6 = 0

for indice, conteudo_linha in df.iterrows():
    if(conteudo_linha["categoria"].lower() == "alimentação"):
        cont1 += 1
    if(conteudo_linha["categoria"].lower() == "transporte"):
        cont2 += 1
    if(conteudo_linha["categoria"].lower() == "hospedagem"):
        cont3 += 1
    if(conteudo_linha["categoria"].lower() == "material de escritório"):
        cont4 += 1
    if(conteudo_linha["categoria"].lower() == "cursos"):
        cont5 += 1
    if(conteudo_linha["categoria"].lower() == "consultoria"):
        cont6 += 1 

if(cont1 > cont2 and cont1 > cont3 and cont1 > cont4 and cont1 > cont5 and cont1 > cont6):
    print(f"A categoria com maior registros de gastos foi: alimentação")
if(cont2 > cont1 and cont2 > cont3 and cont2 > cont4 and cont2 > cont5 and cont2 > cont6):    
    print(f"A categoria com maior registros de gastos foi: transporte")
if(cont3 > cont2 and cont3 > cont1 and cont3 > cont4 and cont3 > cont5 and cont3 > cont6):
    print(f"A categoria com maior registros de gastos foi: hospedagem")
if(cont4 > cont2 and cont4 > cont3 and cont4 > cont1 and cont4 > cont5 and cont4 > cont6):    
    print(f"A categoria com maior registros de gastos foi: material de escritório")
if(cont5 > cont2 and cont5 > cont3 and cont5 > cont4 and cont5 > cont1 and cont5 > cont6):
    print(f"A categoria com maior registros de gastos foi: cursos")
if(cont6 > cont2 and cont6 > cont3 and cont6 > cont4 and cont6 > cont5 and cont6 > cont1):    
    print(f"A categoria com maior registros de gastos foi: consultoria")    

print("==============================================================================================")
print("Exercício 9")

gastos_por_responsavel = 0
nome = input("Digite o nome de um responsável pelos gastos: ")

for indice, conteudo_linha in df.iterrows():
    if(conteudo_linha["responsável"].lower() == nome.lower()):
        gastos_por_responsavel += conteudo_linha["valor"]
   
print(f"O valor gasto por {nome} foi: {gastos_por_responsavel: .2f}")

print("==============================================================================================")
print("Exercício 10")


# lista_data = []
# resultado = []

# for indice, conteudo_linha in df.iterrows():
    
#     if(conteudo_linha["valor"] > 500):
#         if(conteudo_linha["data"]):
#             lista_data.append(conteudo_linha['data'])

# for data in lista_data:
#     for i in lista_data:
#         if(data == i):
#             resultado.append(data)

# for resp in resultado:
#     print(f"As data em que todos os gastos foram maiores que R$ 500,00 são: {resp}")

for indice, conteudo_linha in df.iterrows():
    if(conteudo_linha["valor"] > 500):
        
        data = conteudo_linha["data"]
    print(f"As datas em que os gastos ultrapassam R$ 500,00 são: {data}")    

# numbers = [75, 51, 92, 24, 62, 88]
# print(f"Lista inicial: {numbers}")
# for i in numbers:
#     print(i)