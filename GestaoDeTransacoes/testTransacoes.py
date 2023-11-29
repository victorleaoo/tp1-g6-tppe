
import unittest
from GestaoTransacoes import GerenciadorDeInventario, ValorInvalidoException

class TesteTransacoesDeInventario(unittest.TestCase):

    def setUp(self):
        self.gerenciador = GerenciadorDeInventario()

    def teste_transacoes_variadas(self):
        # Dados de teste parametrizados
        transacoes = [
            ("recebimento", "12345", 20, "001"),
            ("venda", "12345", 10, "001"),
            ("transferencia", "001", "002", "12345", 5),
            ("devolucao", "12345", 3, "001"),
            ("ajuste", "12345", -2, "001")
        ]

        for transacao in transacoes:
            with self.subTest(transacao=transacao):
                tipo, *args = transacao
                resultado = getattr(self.gerenciador, f"registrar_{tipo}")(*args)
                self.assertTrue(resultado)

                # Verificando se o estoque foi atualizado corretamente
                if tipo != "transferencia":
                    id_produto, _, id_filial = args if tipo != "ajuste" else (args[0], args[1], args[2])
                    estoque_atual = self.gerenciador.consultar_estoque(id_produto, id_filial)
                    self.assertIsNotNone(estoque_atual)

    def teste_transacoes_quantidades_negativas(self):
        # Dados de teste parametrizados
        transacoes = [
            ("venda", "12345", -10, "001"),
            ("transferencia", "001", "002", "12345", -5),
            ("devolucao", "12345", -3, "001")
        ]

        for transacao in transacoes:
            with self.subTest(transacao=transacao):
                tipo, *args = transacao
                with self.assertRaises(ValorInvalidoException):
                    getattr(self.gerenciador, f"registrar_{tipo}")(*args)

    def teste_ajuste_estoque_negativo(self):
        # Testando um ajuste que resultaria em estoque negativo
        id_produto = "12345"
        quantidade_ajuste_negativa = -100  # Supondo que isso exceda o estoque existente
        id_filial = "001"
        with self.assertRaises(ValorInvalidoException):
            self.gerenciador.registrar_ajuste(id_produto, quantidade_ajuste_negativa, id_filial)
