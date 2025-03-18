nome = input("Qual seu nome?: ")
idade = input("Qual sua idade?: ")
cidade = input("Onde você mora?: ")
altura = input("E qual sua altura?: ")

print(f"Olá, {nome}, sua idade é {idade} anos, e sua altura é {altura}")
print(f"Você mora em {cidade}")
print(f"Os quatro tipos de variáveis:")

number = 18
string = "nome"
floatType = float(314)
booleanType = True

print(type(number))
print(type(string))
print(type(floatType))
print(type(booleanType))