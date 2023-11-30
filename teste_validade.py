# -*- coding: utf-8 -*-
import pytest
from produto import Produto, DescricaoEmBrancoException
from datetime import datetime, timedelta

def test_cadastro_produto():
    data_atual = datetime.now()

    produto = Produto(
        nome="Shampoo Suave",
        codigo_barras="123456789",
        preco_compra=5.50,
        preco_venda=15.20,
        quantidade_inicial=10,
        lote=0,
        data_validade="12/01/2022"
    )

    assert produto.nome == "Shampoo Suave"
    assert produto.codigo_barras == "123456789"
    assert produto.preco_compra == 5.50
    assert produto.preco_venda == 15.20
    assert produto.quantidade_inicial == 10
    assert produto.lote == 0
    assert produto.data_validade == "12/01/2022"

    # Converta a data de validade do produto para um objeto datetime
    data_validade_produto = datetime.strptime(produto.data_validade, "%d/%m/%Y")

 
    # Verifique se o produto está dentro do período de validade (data de validade maior ou igual à data atual)
    assert data_validade_produto >= data_atual
  

