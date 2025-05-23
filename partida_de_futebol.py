import pandas as pd
import random

df = pd.read_csv("partidas_futebol_sem_gols.csv", sep = ';' )# parâmetro sep para pegar o separador pelo ";"

print("=============================================================================================")
print("Parte 1: Simulação do placar com base em força de ataque")
print("=============================================================================================")
linha = input("Escolha uma linha para jogar: ")
print("=============================================================================================")
indice_escolhido = int(linha)

for indice, conteudo_linha in df.iterrows():
    if(indice == indice_escolhido):

        forca_attack_casa = 0
        forca_attack_fora = 0
        gol_casa = 0
        gol_fora = 0
        aproveitamento_casa = 0
        aproveitamento_fora = 0
        agressividade = 0
        ipo_casa = 0
        ipo_fora = 0
        pressao_tatica_casa = 0
        pressao_tatica_fora = 0
        contador_ciclos_casa = 0
        contador_ciclos_fora = 0

        print(f"{conteudo_linha['TimeCasa']} x {conteudo_linha['TimeFora']}")

        limite_forca_casa = random.randint(1, 101)
        limite_forca_fora = random.randint(1, 101)

        for index in range(1, limite_forca_casa):
            forca_attack_casa = forca_attack_casa + 1

        while(forca_attack_casa >= 10):
            forca_attack_casa = forca_attack_casa - 10
            gol_casa += 1

        for index in range(1, limite_forca_fora):
            forca_attack_fora = forca_attack_fora + 1

        while(forca_attack_fora >= 10):
            forca_attack_fora = forca_attack_fora - 10
            gol_fora += 1
#=============================================================================================================================================================
        print("=============================================================================================") 
        if(gol_casa > gol_fora):
            print(f"O {conteudo_linha['TimeCasa']}(time da casa) fez {gol_casa} gols contra {gol_fora} gols do {conteudo_linha['TimeFora']}(time visitante) e venceu a partida!")

            print("=============================================================================================")
            print("Parte 2: Estatísticas da Partida | Aproveitamento ofensivo")
            aproveitamento = (gol_casa / conteudo_linha["Chutes_Casa"]) * 100
            print(f"O aproveitamento do {conteudo_linha['TimeCasa']}(time da casa) foi {aproveitamento:.2f}")

        elif(gol_casa == gol_fora):
            print(f"Empate!! {conteudo_linha['TimeCasa']}(time da casa) e {conteudo_linha['TimeFora']}(time visitante) ficaram em {gol_casa} X {gol_fora}")
            print("=============================================================================================")
            print("Parte 2: Estatísticas da Partida | Aproveitamento ofensivo")

            aproveitamento_casa = (gol_casa / conteudo_linha["Chutes_Casa"]) * 100

            print(f"O aproveitamento do {conteudo_linha['TimeCasa']} foi {aproveitamento_casa:.2f}")

            print("=============================================================================================")

            aproveitamento_fora = (gol_fora / conteudo_linha["Chutes_Fora"]) * 100

            print(f"O aproveitamento do {conteudo_linha['TimeFora']} foi {aproveitamento_fora:.2f}")

        else:
            print(f"O {conteudo_linha['TimeFora']} fez {gol_fora} gols contra {gol_casa} gols do {conteudo_linha['TimeCasa']} e venceu a partida!")
            if(gol_fora > 0):
                print("=============================================================================================")
                print("Parte 2: Estatísticas da Partida | Aproveitamento ofensivo")

                aproveitamento = (gol_fora / conteudo_linha["Chutes_Fora"]) * 100
                print(f"O aproveitamento do {conteudo_linha['TimeFora']} foi {aproveitamento:.2f}")
#=============================================================================================================================================================        
        print("=============================================================================================")
        if(conteudo_linha["Faltas_Casa"] > conteudo_linha["Faltas_Fora"]):
            print("2. Time mais agressivo")
            print("=============================================================================================")

            agressividade = conteudo_linha["Faltas_Casa"] + (2 * conteudo_linha["CA_Casa"]) +( 3 * conteudo_linha["CV_Casa"])
            print(f"O time mais agressivo foi {conteudo_linha['TimeCasa']} e a agressividade foi de: {agressividade:.2f}%")

        if(conteudo_linha["Faltas_Fora"] > conteudo_linha["Faltas_Casa"]):
            print("2. Time mais agressivo")
            

            agressividade = conteudo_linha["Faltas_Fora"] + (2 * conteudo_linha["CA_Fora"]) +( 3 * conteudo_linha["CV_Fora"])
            print(f"O time mais agressivo foi {conteudo_linha['TimeFora']} e a agressividade foi de: {agressividade:.2f}%")
#=============================================================================================================================================================
        print("=============================================================================================")
        print("3. Comparação de escanteios")
    
        if(conteudo_linha["Escanteios_Casa"] > conteudo_linha["Escanteios_Fora"]):
            total_esc_casa = conteudo_linha["Escanteios_Casa"] - conteudo_linha["Escanteios_Fora"]
            print(f"O time que teve mais escanteios foi: {conteudo_linha['TimeCasa']} com {total_esc_casa} no total!")

        elif(conteudo_linha["Escanteios_Casa"] == conteudo_linha["Escanteios_Fora"]):
                print(f"Os dois times tiveram o mesmo número de escanteios!")

        else:    
            total_esc_fora = conteudo_linha["Escanteios_Fora"] - conteudo_linha["Escanteios_Casa"]
            print(f"O time que teve mais escanteios foi: {conteudo_linha['TimeFora']} com {total_esc_fora} no total!")

#=============================================================================================================================================================            
        print("=============================================================================================")
        print("4. Pressa ofensiva")

        ipo_casa = conteudo_linha["Impedimentos_Casa"] / (conteudo_linha["Chutes_Casa"] + conteudo_linha["Escanteios_Casa"] + 1)
        print(f"O Índice de Pressa Ofensiva (IPO) do {conteudo_linha['TimeCasa']} foi {ipo_casa:.2f}")

        ipo_fora = conteudo_linha["Impedimentos_Fora"] / (conteudo_linha["Chutes_Fora"] + conteudo_linha["Escanteios_Fora"] + 1)
        print(f"O Índice de Pressa Ofensiva (IPO) do {conteudo_linha['TimeFora']} foi {ipo_fora:.2f}")
#=============================================================================================================================================================
        print("=============================================================================================")
        print("Parte 3: Simulação da pressão tática")
        limite_casa = random.randint(50, 151)
        limite_fora = random.randint(50, 151)

        while(pressao_tatica_casa < limite_casa):
            pressao_tatica_casa += (conteudo_linha["Escanteios_Casa"] * 1.5) + (conteudo_linha["Chutes_Casa"] * 1.2) + (conteudo_linha["Faltas_Casa"] * 0.5)
            contador_ciclos_casa += 1

        while(pressao_tatica_fora < limite_fora):
            pressao_tatica_fora += (conteudo_linha["Escanteios_Fora"] * 1.5) + (conteudo_linha["Chutes_Fora"] * 1.2) + (conteudo_linha["Faltas_Fora"] * 0.5)
            contador_ciclos_fora += 1

        print(f"O Índice de Pressão Tática do {conteudo_linha['TimeCasa']} foi {pressao_tatica_casa:.2f}")
        print(f"O time {conteudo_linha['TimeCasa']} conseguiu {contador_ciclos_casa} ciclos de ataque!")
        print("=============================================================================================")
        print(f"O Índice de Pressão Tática do {conteudo_linha['TimeFora']} foi {pressao_tatica_fora:.2f}")
        print(f"O time {conteudo_linha['TimeFora']} conseguiu {contador_ciclos_fora} ciclos de ataque!")

print("=============================================================================================")
