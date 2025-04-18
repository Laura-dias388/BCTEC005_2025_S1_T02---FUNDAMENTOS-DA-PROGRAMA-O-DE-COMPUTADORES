import tkinter as tk

def dizer_ola():
    nome = entrada_nome.get()
    resultado.config(text=f"Olá, {nome}!")

# Cria a janela
janela = tk.Tk()
janela.title("Interface com Python")
janela.geometry("300x150")

# Widgets
tk.Label(janela, text="Digite seu nome:").pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

tk.Button(janela, text="Dizer Olá", command=dizer_ola).pack()
resultado = tk.Label(janela, text="")
resultado.pack()

# Roda a interface
janela.mainloop()
