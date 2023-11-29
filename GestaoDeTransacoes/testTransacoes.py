# test_inventario.py
import unittest
from GestaoTransacoes import GerenciadorDeInventario, ValorInvalidoException

class TesteTransacoesDeInventario(unittest.TestCase):

    def teste_registrar_transacao_venda(self):
        # Criando uma instância do gerenciador de inventário
        gerenciador = GerenciadorDeInventario()

        # Dados fictícios para a transação
        id_produto = "12345"
        quantidade = 10

        # Tentativa de registrar uma transação de venda
        resultado = gerenciador.registrar_venda(id_produto, quantidade)

        # Verificando se a transação foi registrada corretamente
        self.assertTrue(resultado)

