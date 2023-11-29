class DescricaoEmBrancoException(Exception):
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
        if (nome is None):
            raise DescricaoEmBrancoException("Todos os atributos devem estar presentes!")

        self.nome = nome
        self.codigo_barras = codigo_barras
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.quantidade_inicial = quantidade_inicial
        self.lote = lote
        self.data_validade = data_validade