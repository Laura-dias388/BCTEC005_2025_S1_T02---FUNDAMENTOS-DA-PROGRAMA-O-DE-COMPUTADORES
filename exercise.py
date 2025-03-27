print(f"=====================================================================================================")
print(f"Exercício 1")

def input_function():
    nome = input("Digite seu nome?: ")
   
    while True:
        try:
            idade = int(input("Digite sua idade?: "))
            break
        except ValueError:
            print("Por favor, digite um número válido para a idade.")
            
    cidade = input("Em qual cidade você mora?: ")

    # nome deve ser string, idade deve ser inteiro e cidade deve ser string


    print(f"Olá, {nome}, sua idade é {idade} anos")
    print(f"Você mora em {cidade}")    
input_function()


print(f"=====================================================================================================")

print(f"Exercício 2")

def types():

    nome2 = "Laura Vital"
    idade2 = 36
    altura2 = 1.63
    
    # nome2 deve ser string idade2 deve ser inteiro e altura2 deve ser float

    print(nome2)
    print(idade2)
    print(altura2)


print(f"=====================================================================================================")

print(f"Exercício 3")

number = 18
string = "nome"
floatType = 3.14
booleanType = True

print(f"Os quatro tipos de variáveis são:")
print(f" Tipo inteiro", type(number))
print(f" Tipo string", type(string))
print(f" Tipo float", type(floatType))
print(f" Tipo boolean", type(booleanType))

print(f"=====================================================================================================")

print(f"Exercício 4")

number01 = input(f"Digite um número: ")
number02 = input(f"Digite outro número: ")

soma = int(number01) + int(number02)
subtracao = int(number01) - int(number02)
divisao = int(number01) // int(number02)
multiplicacao = int(number01) * int(number02)

print(f"A soma dos números digitados é: {soma}")
print(f"A subtração dos números digitados é: {subtracao}")
print(f"A divisão dos números digitados é: {divisao}")
print(f"A multiplicação dos números digitados é: {multiplicacao}")

print(f"=====================================================================================================")

print(f"Exercício 5")

nome3 = input(f"Digite o nome do aluno: ")
matricula = input(f"Digite o número da matrícula: ")

print(f"Seja bem vindo(a): {nome3}, matrícula: {matricula} à disciplina de Fundamentos de Programação de Computadores do BCTec.")

print(f"=====================================================================================================")

print(f"Exercício 6")

primeiro_nome = input(f"Digite seu primeiro nome: ")
ultimo_nome = input(f"Digite seu sobrenome: ")

nome_completo = primeiro_nome + " " + ultimo_nome

print(f"Seu nome completo é: {nome_completo}")

print(f"=====================================================================================================")

print(f"Exercício 7")

num1 = input(f"Digite um número natural: ")
num2 = input(f"Digite outro número natural: ")

somando = int(num1) + int(num2)

print(f"O resultado da soma desses dois números que você digitou será: {somando}")

print(f"=====================================================================================================")

print(f"Exercício 8")

a = 1
b = 2 
c = 3

print(f"As três variáveis sao: {a, b , c}")

print(f"=====================================================================================================")

print(f"Exercício 9")

x = 10
y = 20

x = 50
y = 100

print(f"Os valores de X e Y agora são: {x, y}")

print(f"=====================================================================================================")

print(f"Exercício 10")

number1 = input(F"Digite um primeiro número: ")
number2 = input(F"Digite um segundo número: ")
number3 = input(F"Digite um terceiro número: ")
    
soma_tres = int(number1) + int(number2) + int(number3)
produto_tres = int(number1) * int(number2) * int(number3)
media_aritmetica = soma_tres / 3

print(f"As três operações foram, soma que resultou em : {soma_tres},\n"
      f"produto que resultou em: {produto_tres} e média aritimética resultou em: {media_aritmetica}")
