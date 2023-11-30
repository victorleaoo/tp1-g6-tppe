import pytest
from produto import Produto, DescricaoEmBrancoException

def test_consulta_estoque_nome():
    produto = Produto("123456789", 10.0, 15.0, 10, "Lote A", "2023-12-31","Produto A")
    resultado_consulta = produto.consulta_estoque_nome()
    assert resultado_consulta == "Produto A"  