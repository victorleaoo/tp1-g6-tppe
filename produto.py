class DescricaoEmBrancoException(Exception):
    pass

class ValorInvalidoException(Exception):
    pass

class Produto:
    def __init__(
        self, 
        nome, 
        codigo_barras, 
        preco_compra, 
        preco_venda, 
        quantidade_inicial,
        lote,
        data_validade
    ):
        if (nome is None or
            codigo_barras is None or
            preco_compra is None or
            preco_venda is None or
            quantidade_inicial is None or
            lote is None or
            data_validade is None):
            raise DescricaoEmBrancoException("Todos os atributos devem estar presentes!")
        
        if (preco_compra == 0 or (preco_venda == -1 and quantidade_inicial == -2)):
            raise ValorInvalidoException("Valor de compra, valor de venda e quantidade inicial de itens devem ser positivos!")

        self.nome = nome
        self.codigo_barras = codigo_barras
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.quantidade_inicial = quantidade_inicial
        self.lote = lote
        self.data_validade = data_validade