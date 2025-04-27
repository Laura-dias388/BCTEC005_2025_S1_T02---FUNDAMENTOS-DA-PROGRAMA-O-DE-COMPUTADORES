# Explicação sobre `__main__` no Python

## O que é `__main__`?

No Python, o código dentro do bloco `if __name__ == "__main__":` é executado **somente quando o script é executado diretamente** e **não quando o módulo é importado** em outro script.

### O que significa `__name__`?

O valor de `__name__` depende de como o script Python é executado:
- **Quando o script é executado diretamente** (por exemplo, `python meu_script.py`), o valor de `__name__` será igual a `"__main__"`.
- **Quando o script é importado em outro arquivo** (por exemplo, `import meu_script`), o valor de `__name__` será igual ao nome do módulo (sem a extensão `.py`).

### Por que usar `if __name__ == "__main__"`?

Esse bloco condicional permite que o código dentro dele seja executado apenas quando o script for executado diretamente. Isso é útil quando você deseja garantir que partes do código (como testes ou a execução de um programa) não sejam executadas quando o script for importado como módulo em outro programa.

### Exemplo de código

```python
def saudacao(nome):
    return f"Olá, {nome}!"

def despedida(nome):
    return f"Tchau, {nome}!"

# Código dentro de __main__
if __name__ == "__main__":
    nome_usuario = "Carlos"
    print(saudacao(nome_usuario))
    print(despedida(nome_usuario))
