def chamada_para_modelo_generativo_fake():
    raise Exception("Função não implementada")

class Calculadora:
    def __init__(self):
        pass

    def calculo_complexo(self, text) -> float | int:

        if isinstance(text, str):
            answer = chamada_para_modelo_generativo_fake()
            return answer.strip()
        else:
            raise TypeError("O argumento text deve ser uma string")
        
    def adicao(self, num1, num2) -> float | int:
        return num1 + num2

    def subtracao(self, num1, num2) -> float | int:
        return num1 - num2

    def multiplicacao(self, num1, num2) -> float | int:
        return num1 * num2

    def divisao(self, num1, num2) -> float | int:
        try:
            return num1 / num2
        except ZeroDivisionError as e:
            raise ZeroDivisionError("Divisão por zero não é permitida")




