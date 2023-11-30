import pytest
from produto import Produto, DescricaoEmBrancoException

def test_consulta_estoque_nome():
    produto = Produto("Produto A","123456789", 10.0, 15.0, 10, "Lote A", "2023-12-31")
    resultado_consulta = produto.consulta_estoque_nome("Produto A")
    assert resultado_consulta == "Produto A"  