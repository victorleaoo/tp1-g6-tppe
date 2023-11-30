import pytest
from produto import Produto, DescricaoEmBrancoException

def test_alerta_estoque_baixo_falha():
    produto = Produto("Produto A", "1234567890", 10.0, 15.0, 10, "Lote A", "2023-12-31")
    assert produto.verificar_estoque_baixo() == False


