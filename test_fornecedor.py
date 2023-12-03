import unittest
from fornecedor import Fornecedor

class TestFornecedor(unittest.TestCase):
    def test_criar_fornecedor_valido(self):
        fornecedor = Fornecedor(1, "Fornecedor A", "Endereço A", "2023-01-01")
        self.assertEqual(fornecedor.id, 1)
        self.assertEqual(fornecedor.nome, "Fornecedor A")
        self.assertEqual(fornecedor.endereco, "Endereço A")
        self.assertEqual(fornecedor.data_contrato, "2023-01-01")