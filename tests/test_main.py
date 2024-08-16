import pytest
from unittest.mock import patch

@patch("src.main.chamada_para_modelo_generativo_fake")
def test_calculo_complexo(mock, calculadora):

    text = "Qual a raiz quadrada de 49?"
    mock.return_value = " 7 "
    assert calculadora.calculo_complexo(text) == "7"

def test_calculo_complexo_erro(calculadora):
    
    text = 49
    with pytest.raises(Exception):
        calculadora.calculo_complexo(text)

def test_adicao(calculadora):
    assert calculadora.adicao(1, 2) == 3

def test_subtracao(calculadora):
    assert calculadora.subtracao(5, 3) == 2

def test_multiplicacao(calculadora):
    assert calculadora.multiplicacao(4, 2) == 8

@pytest.mark.parametrize("entrada, saida", [((0,5), 0), ((8,4), 2)])
def test_divisao(entrada, saida, calculadora):
    x, y = entrada
    assert calculadora.divisao(x,y) == saida

def test_divisao_error(calculadora):
    with pytest.raises(Exception):
        calculadora.divisao(5, 0)


