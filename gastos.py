import pandas as pd
#import matplotlib.pyplot as plt

df = pd.read_csv("gastos.csv")
#print(df)

#soma = df["valor"].sum()
#print(f"SOMA: {soma:.2f}")


soma = 0
for indice, conteudo_linha in df.iterrows():
    # q 1
    #if(conteudo_linha["valor"]> 1000):
    #   print(f" alerta, responsável: {conteudo_linha['responsável']} gastou: {conteudo_linha['valor']} ")

    if(conteudo_linha["categoria"] == "Cursos"):
        soma +=  conteudo_linha['valor']  
    
print(f"Soma dos valores da categoria cursos: {soma:.2f}") 

    




#gastos = df.groupby("categoria")['valor'].sum()
#plt.bar (gastos.index, gastos.values)
#plt.xticks(rotation = 45)
#plt.show()