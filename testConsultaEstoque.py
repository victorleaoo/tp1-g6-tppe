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

    import pytest
from produto import Produto

test_data = [
    ("123456789", 10.0, 15.0, 100, "Lote A", "2023-12-31", "Produto A"),
    ("987654321", 12.5, 18.0, 80, "Lote B", "2024-05-15", "Produto B"),
    ("111222333", 8.0, 12.0, 50, "Lote C", "2023-08-20", "Produto C"),
    ("444555666", 15.0, 20.0, 200, "Lote D", "2024-10-10", "Produto D"),
    ("777888999", 20.0, 25.0, 300, "Lote E", "2023-06-30", "Produto E"),
]

@pytest.mark.parametrize(
    "codigo_barras, preco_compra, preco_venda, quantidade_inicial, lote, data_validade, nome",
    test_data
)
def test_consulta_estoque_nome(codigo_barras, preco_compra, preco_venda, quantidade_inicial, lote, data_validade, nome):
    produto = Produto(codigo_barras, preco_compra, preco_venda, quantidade_inicial, lote, data_validade, nome)
    resultado_consulta = produto.consulta_estoque_nome(produto.nome)
    assert resultado_consulta == produto

@pytest.mark.parametrize(
    "codigo_barras, preco_compra, preco_venda, quantidade_inicial, lote, data_validade, nome",
    test_data
)
def test_consulta_estoque_codigo(codigo_barras, preco_compra, preco_venda, quantidade_inicial, lote, data_validade, nome):
    produto = Produto(codigo_barras, preco_compra, preco_venda, quantidade_inicial, lote, data_validade, nome)
    resultado_consulta = produto.consulta_estoque_codigo(produto.codigo_barras)
    assert resultado_consulta == produto

@pytest.mark.parametrize(
    "codigo_barras, preco_compra, preco_venda, quantidade_inicial, lote, data_validade, nome",
    test_data
)
def test_consulta_estoque(codigo_barras, preco_compra, preco_venda, quantidade_inicial, lote, data_validade, nome):
    produto = Produto(codigo_barras, preco_compra, preco_venda, quantidade_inicial, lote, data_validade, nome)
    resultado_consulta = produto.consulta_estoque(produto.nome, produto.codigo_barras)
    assert resultado_consulta == produto
