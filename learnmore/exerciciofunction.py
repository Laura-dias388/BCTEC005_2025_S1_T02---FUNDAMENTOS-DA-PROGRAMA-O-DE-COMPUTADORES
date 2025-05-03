# arquivo: exercicios.py

def exercicio1(a, b):
    resultado = []
    if a > 10:
        resultado.append("A > 10")
    if a + b == 20:
        resultado.append("A + B == 20")
    else:
        resultado.append("Número não válido")
    return resultado

def exercicio2(a, b):
    if a < 10:
        return ["A < 10"]
    elif a + b == 20:
        return ["A + B == 20"]
    else:
        return ["Número não válido"]

def exercicio3(a, b):
    resultado = []
    if a == 10:
        resultado.append("A == 10")
    if a + b == 20:
        resultado.append("A + B == 20")
    if b == 10:
        resultado.append("B == 10")
    return resultado

def exercicio4(a, b):
    if (a > 10) or (a + b == 20):
        return ["Número válido!"]
    elif a == b:
        return ["A é igual B"]
    elif (a != 10) and (b != 10):
        return ["Número não válido"]

def exercicio5(a, b):
    resultado = []
    if a > 10:
        resultado.append("A > 10")
    else:
        resultado.append("A <= 10")

    if a + b == 20:
        resultado.append("A + B == 20")
    else:
        resultado.append("A + B != 20")
    return resultado

def exercicio6(a, b):
    if (a > 10) and (a + b == 20):
        return ["A + B == 20"]
    else:
        return ["Número não válido"]

def exercicio7(a, b):
    if a > 10:
        return ["A é maior que 10"]
    elif a + b == 20:
        return ["A + B == 20"]
    else:
        return ["Número não válido"]

def exercicio8(a, b):
    if (a > 10) or (a + b == 20):
        return ["A + B == 20"]
    else:
        return ["Número não válido"]

def exercicio9(a, b):
    if (a > 10) or (a + b == 20):
        return ["Número válido!!"]
    elif a == b:
        return ["A é igual B"]
    elif (a != 10) and (b != 10) and (a < 10):
        return ["A é menor que 10"]
    else:
        return ["Número não válido!!"]

def exercicio10(a, b):
    if (a > 10) or (a + b == 20):
        return ["Números válidos!"]
    else:
        return ["Número não válido"]
