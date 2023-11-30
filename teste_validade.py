# -*- coding: utf-8 -*-
import pytest
from produto import Produto, DescricaoEmBrancoException
from datetime import datetime, timedelta

def test_produto_fora_validade():
    data_atual = datetime.now()
    produto = Produto(
        nome="Shampoo na validade",
        codigo_barras="123456789",
        preco_compra=5.50,
        preco_venda=15.20,
        quantidade_inicial=10,
        lote=0,
        data_validade= "12/01/1999"
    )
    assert produto.esta_no_periodo_de_validade() == False

def test_produto_na_validade():
    with pytest.raises(DescricaoEmBrancoException):
        produto = Produto(
            nome="Shampoo na validade",
            codigo_barras="123456789",
            preco_compra=5.50,
            preco_venda=15.20,
            quantidade_inicial=10,
            lote=0,
            data_validade=""
        )
    assert "produto" not in locals()