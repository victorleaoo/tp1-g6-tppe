import unittest
from fornecedor import Fornecedor

class TestFornecedor(unittest.TestCase):
    def test_criar_fornecedor_valido(self):
        fornecedor = Fornecedor(1, "Fornecedor A", "Endereço A", "2023-01-01")
        self.assertEqual(fornecedor.id, 1)
        self.assertEqual(fornecedor.nome, "Fornecedor A")
        self.assertEqual(fornecedor.endereco, "Endereço A")
        self.assertEqual(fornecedor.data_contrato, "2023-01-01")

    def test_criar_fornecedor_com_id_invalido(self):
        with self.assertRaises(ValueError):
            Fornecedor(None, "Fornecedor B", "Endereço B", "2023-01-01")
    
    def test_criar_fornecedor_com_id_invalido_vazio(self):
        with self.assertRaises(ValueError):
            Fornecedor('', "Fornecedor C", "Endereço C", "2023-01-01")

    def test_criar_fornecedor_id_string(self):
        with self.assertRaises(ValueError):
            Fornecedor("abc", "Fornecedor D", "Endereço D", "2023-01-01")
        
if __name__ == '__main__':
    unittest.main()
