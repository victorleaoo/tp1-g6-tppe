import pytest
from produto import Produto, DescricaoEmBrancoException

def test_alerta_estoque_baixo():
    produto = Produto("Produto A", "1234567890", 10.0, 15.0, 5, "Lote A", "2023-12-31")
    assert produto.verificar_estoque_baixo() == True


def test_alteracao_limite_estoque():
    produto = Produto("Produto F", "4444444444", 50.0, 70.0, 25, "Lote F", "2024-12-31")
    assert produto.verificar_estoque_baixo() == False 

    produto.limite_estoque = 30
    assert produto.verificar_estoque_baixo() == True  

def test_limite_estoque():
    produto = Produto("Produto A", "1234567890", 10.0, 15.0, 10, "Lote A", "2023-12-31")
    assert produto.verificar_estoque_baixo() == True