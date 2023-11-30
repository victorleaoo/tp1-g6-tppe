import pytest
from produto import Produto, DescricaoEmBrancoException, ValorInvalidoException

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

test_data = [
    (None, "123456789", 10.0, 20.0, 50, "11", "22/10/2026"),
    ("Shampoo", None, 5.0, 10.0, 20, "22", "12/02/2030"),
    ("Sabonete", "987654321", None, 1.0, 1, "33", "01/01/2024"),
    ("Tenis", "123987456", 49.99, None, 500, "44", "09/06/2096"),
    ("Computador", "000000000", 22.22, 157.55, None, "55", "07/07/2027"),
    ("Camisa", "998888444", 59.10, 299.99, 11, None, "11/11/2111"),
    ("Presunto", "123321213", 10.0, 20.0, 22, "66", None),
]

@pytest.mark.parametrize(
    "nome, codigo_barras, preco_compra, preco_venda, quantidade_inicial, lote, data_validade",
    test_data
)
def test_produto_missing_arguments(nome, codigo_barras, preco_compra, preco_venda, quantidade_inicial, lote, data_validade):
    with pytest.raises(DescricaoEmBrancoException):
        produto = Produto(
            nome, codigo_barras, preco_compra, preco_venda, quantidade_inicial, lote, data_validade
        )

def test_cadastro_produto_com_preco_compra_invalido():
    with pytest.raises(ValorInvalidoException):
        Produto(
            nome="Produto com preco de compra invalido",
            codigo_barras="123321123",
            preco_compra=0,
            preco_venda=10, 
            quantidade_inicial=2,
            lote="02",
            data_validade="01/01/2025"
        )