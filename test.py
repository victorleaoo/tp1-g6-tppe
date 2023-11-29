import pytest
from produto import Produto, DescricaoEmBrancoException

def test_cadastro_produto():
    produto = Produto(
        nome="Shampoo Suave",
        codigo_barras="123456789",
        preco_compra=5.50,
        preco_venda=15.20,
        quantidade_inicial=10,
        lote=0,
        data_validade="12/01/2024"
    )

    assert produto.nome == "Shampoo Suave"
    assert produto.codigo_barras == "123456789"
    assert produto.preco_compra == 5.50
    assert produto.preco_venda == 15.20
    assert produto.quantidade_inicial == 10
    assert produto.lote == 0
    assert produto.data_validade == "12/01/2024"

def test_produto_missing_arguments():
    with pytest.raises(DescricaoEmBrancoException):
        produto = Produto(
            None, "123456789", 10.0, 20.0, 50, "1", "22/10/2026"
        )

def test_produto_missing_arguments_dois():
    with pytest.raises(DescricaoEmBrancoException):
        produto = Produto(
            "Tenis Nike", None, 150.20, 400.0, 1, "2", "15/12/2022"
        )