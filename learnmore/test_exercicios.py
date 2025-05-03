# arquivo: test_exercicios_pytest.py

import exerciciofunction  # importa suas funções

def test_exercicio1():
    assert exerciciofunction.exercicio1(9, 11) == ["Número não válido"]

def test_exercicio2():
    assert exerciciofunction.exercicio2(20, 11) == ["Número não válido"]

def test_exercicio3():
    assert exerciciofunction.exercicio3(11, 10) == ["A + B == 20", "B == 10"]

def test_exercicio4():
    assert exerciciofunction.exercicio4(9, 12) == ["Número válido!"]

def test_exercicio5():
    assert exerciciofunction.exercicio5(12, 9) == ["A > 10", "A + B != 20"]

def test_exercicio6():
    assert exerciciofunction.exercicio6(12, 8) == ["A + B == 20"]

def test_exercicio7():
    assert exerciciofunction.exercicio7(20, 12) == ["A é maior que 10"]

def test_exercicio8():
    assert exerciciofunction.exercicio8(8, 5) == ["Número não válido"]

def test_exercicio9():
    assert exerciciofunction.exercicio9(10, 91) == ["Número válido!!"]

def test_exercicio10():
    assert exerciciofunction.exercicio10(8, 11) == ["Número não válido"]
