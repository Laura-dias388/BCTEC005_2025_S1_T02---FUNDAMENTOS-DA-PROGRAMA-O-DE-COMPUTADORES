print("-=" * 50)

show = {
    "nome": "Tomorowland",
    "descricao": "Festival",
    "artista": "Charlotte",
    "genero_musical": "Eletrônica"
}

day_festival = {
    "data": "22/08/2025",
    "preco_base": 2000,
    "capacidade_maxima": 500,
}
resp = "S"
total_inscritos = 0
total_arrecadado = 0
brindes_figure = 0
brindes_pop_corn = 0
brindes_choc = 0
brindes_refri = 0

setores = {
    "Pista": {
        "vagas": 4,
        "acrescimo": 0,
        "brindes": []
    },
    "Campo": {
        "vagas": 6,
        "acrescimo": 10,
        "brindes": ["bonequinho do BCTec"]
    },
    "Arquibancada": {
        "vagas": 5,
        "acrescimo": 12,
        "brindes": ["bonequinho do BCTec", "combo de pipoca"]
    },
    "VIP": {
        "vagas": 3,
        "acrescimo": 15,
        "brindes": ["bonequinho do BCTec", "combo de pipoca", "refrigerante", "chocolate"]
        }
    }


while True:
    print("           -------VENDA DE INGRESSOS-------")
    print("-=" * 30)
    

    print(f"               Show disponível {show['nome']}")
    print(f"               Data: {day_festival['data']}")
    print("-=" * 30)

    print(" > Cadastro de cliente <")
    cadastro = {}

    cadastro["nome_completo"] = str(input("=> Digite seu nome completo: "))
    cadastro["CPF"] = str(input("Digite seu CPF, apenas os dígitos: "))

    for k, v in cadastro.items():
        if v == "":
            print(">> O campo não pode ficar vazio, retorne e cadastre novamente!")
            exit()
    if len(cadastro["CPF"]) != 11:
        print(">> O CPF precisa ter onze dígitos, retorne e cadastre novamente!")
        exit()
    print(">> É estudante da BCTec?")
    cadastro["matricula"] = str(input(">> Digite sua matrícula: "))
    total_inscritos += 1

    print("-=" * 30)

    choise = str(input("=> Escolha o setor: Pista, Campo, Arquibancada ou VIP: "))
    print(choise)
    if choise == "Pista":
        setores["Pista"]["vagas"] -= 1
        vaga = setores["Pista"]["vagas"]
        print(f"Sua escolha tem {setores['Pista']['acrescimo']} de acréscimo e nenhum brinde!")
        valor = day_festival["preco_base"]
        
        total_arrecadado += valor

    elif choise == "Campo":
        setores["Campo"]["vagas"] -= 1
        vaga = setores["Campo"]["vagas"]
        print(f"Sua escolha tem {setores['Campo']['acrescimo']}% de acréscimo!")
        print("-=" * 30)
        brindes_figure += 1

        percentual = (day_festival["preco_base"] * (setores["Campo"]['acrescimo'] / 100))
        valor = percentual + day_festival["preco_base"]
        total_arrecadado += valor

        for i in setores["Campo"]["brindes"]:
            print(f"O brinde é: {i}")

    elif choise == "Arquibancada":
        setores["Arquibancada"]["vagas"] -= 1
        vaga = setores["Arquibancada"]["vagas"]
        print(f"Sua escolha tem {setores['Arquibancada']['acrescimo']}% de acréscimo e tem os seguintes brindes!")
        print("-=" * 30)

        for i in setores["Arquibancada"]["brindes"]:
            print(f"-{i}")
        percentual = (day_festival["preco_base"] * (setores["Arquibancada"]['acrescimo'] / 100))
        valor = percentual + day_festival["preco_base"]
        total_arrecadado += valor
        brindes_figure += 1
        brindes_pop_corn += 1

    elif choise == "VIP":
        setores["VIP"]["vagas"] -= 1
        vaga = setores["VIP"]["vagas"]
        print(f"Sua escolha tem {setores['VIP']['acrescimo']}% de acréscimo e tem os seguintes brindes!")
        print("-=" * 30)

        for i in setores["VIP"]["brindes"]:
            print(f"-{i}")
        percentual = (day_festival["preco_base"] * (setores["VIP"]['acrescimo'] / 100))
        valor = percentual + day_festival["preco_base"]
        total_arrecadado += valor
        brindes_figure += 1
        brindes_pop_corn += 1
        brindes_refri += 1
        brindes_choc += 1

    else:
        print("É necessário escolher uma opção para prosseguir")


   
    print("======================================================================================")
    print("- Opções:  PIX")
    print("- Opções:  Dinheiro")
    print("- Opções:  Débito")
    print("- Opções:  Crédito")

    pagamento = input(" >> Escolha sua forma de pagamento: ")

    print("=============EMISSÃO DO BILHETE DIGITAL===============")

    print("-----------Cadastro realizado com sucesso!------------")
    print(f"=> Nome: {cadastro['nome_completo']}")
    print(f"=> CPF: {cadastro['CPF']}")
    print(f"=> Aluno do BCTec: Matrícula => {cadastro['matricula']}")
    print(f"=> Show: {show['nome']}")
    print(f"=> Setor: {choise}")
    # print(f"Preço total: {valor}")
    print(f"=> Forma de pagamento: {pagamento}")
    # print(f"Lista de brindes: {setores[choise]['brindes']}")
    continuar = input("Deseja cadastrar outro cliente? (S/N): ").upper()
    if continuar != "S":
        break

print("=============RELATÓRIO ADMINISTRATIVO===============")

print(f"- Total de inscritos: {total_inscritos}")

for v in cadastro["nome_completo"]:
    print(f"Nomes: {v}")
print(f"- Total arrecadado: R$ {total_arrecadado:.2f}")

print(f"- O total de bonequinhos BCTec foi {brindes_figure}")
print(f"- O total de combo de pipoca foi {brindes_pop_corn}")
print(f"- O total de chocolate foi {brindes_choc} e refrigerante foi {brindes_refri}")
# print(f"- Vagas restantes por setor: {vaga}")
for setor, dados in setores.items():
    print(f"- {setor}: {dados['vagas']} vagas restantes")