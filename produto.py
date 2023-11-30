class DescricaoEmBrancoException(Exception):
    pass

class Produto:
    def __init__(
        self, 
        codigo_barras, 
        preco_compra, 
        preco_venda, 
        quantidade_inicial,
        lote,
        data_validade,
        nome
    ):
        if (nome is None or
            codigo_barras is None or
            preco_compra is None or
            preco_venda is None or
            quantidade_inicial is None or
            lote is None or
            data_validade is None):
            raise DescricaoEmBrancoException("Todos os atributos devem estar presentes!")

        self.nome = nome
        self.codigo_barras = codigo_barras
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.quantidade_inicial = quantidade_inicial
        self.lote = lote
        self.data_validade = data_validade


    def consulta_estoque_nome(self, nome):
        if self.nome == nome:
            return self

    def consulta_estoque_codigo(self, codigo): 
        if self.codigo_barras == codigo: 
            return self 