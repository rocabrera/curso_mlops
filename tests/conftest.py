import pytest
from src.main import Calculadora

@pytest.fixture
def calculadora():
    # Crie uma instância da classe Calculadora
    calc = Calculadora()
    # Realize qualquer configuração ou preparação necessária
    # Retorne a instância da classe Calculadora
    yield calc
    # Realize qualquer limpeza ou finalização necessária