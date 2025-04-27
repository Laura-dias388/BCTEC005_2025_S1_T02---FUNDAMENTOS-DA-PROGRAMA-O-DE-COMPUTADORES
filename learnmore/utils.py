def hello():
    print("Olá do utils!")

if __name__ == "__main__":
    print("Executando utils diretamente!")
    hello()
# O __name__ é uma variável especial que o Python cria
#  automaticamente toda vez que você executa ou importa um arquivo .py.

# Você não precisa criar o __name__ 
# — ele já existe pra todo arquivo Python, sem você fazer nada.

# Todo arquivo .py recebe um crachá (__name__) do Python:

# Se ele foi chamado diretamente: crachá = "__main__"

# Se ele foi importado: crachá = "nome do arquivo"

# O if __name__ == "__main__" é só um porteiro 
# conferindo o crachá antes de deixar o código entrar na festa. 🪪🎉