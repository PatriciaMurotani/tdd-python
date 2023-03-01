import pytest

from pytest import mark
from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_06_04_1992_deve_retornar_31(self):
        #Given
        entrada = '06/04/1992'
        esperado = 31

        #When
        funcionario_teste = Funcionario('Teste', entrada, 2000)
        resultado = funcionario_teste.idade()

        #Then
        assert resultado == esperado

    def test_quando_sobrenome_recebe_Patricia_Murotani_deve_retornar_Murotani(self):
        entrada = 'Patricia Murotani'
        esperado = 'Murotani'

        patricia = Funcionario(entrada, '12/12/2000', 2000)
        resultado = patricia.sobrenome()

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Bartolomeu Santos'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '12/12/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario_teste = Funcionario('teste', '05/05/1995', entrada)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 1000000

            funcionario_teste = Funcionario('teste', '05/05/1995', entrada)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado

