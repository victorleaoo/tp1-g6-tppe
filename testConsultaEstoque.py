import pytest
from produto import Produto, DescricaoEmBrancoException

def test_consulta_estoque_nome():
    produto = Produto("123456789", 10.0, 15.0, 10, "Lote A", "2023-12-31","Produto A")
    resultado_consulta = produto.consulta_estoque_nome(produto.nome)
    assert resultado_consulta == produto

def test_consulta_estoque_codigo():
    produto = Produto("123456789", 10.0, 15.0, 10, "Lote A", "2023-12-31","Produto B")
    resultado_consulta = produto.consulta_estoque_codigo(produto.codigo_barras)
    assert resultado_consulta == produto 

#O produto pode ter o mesmo nome, mas não o mesmo codigo.
def test_consulta_estoque():
    produto = Produto("123456789", 10.0, 15.0, 10, "Lote A", "2023-12-31","Produto B")
    resultado_consulta = produto.consulta_estoque(produto.nome,produto.codigo_barras)
    assert resultado_consulta == produto 