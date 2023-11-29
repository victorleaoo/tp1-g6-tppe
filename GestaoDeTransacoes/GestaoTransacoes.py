class ValorInvalidoException(Exception):
    pass

class GerenciadorDeInventario:
    def __init__(self):
        # Inicializa o estoque com alguns dados de exemplo
        self.estoque = {'12345': {'001': 50, '002': 30}}

    def registrar_recebimento(self, id_produto, quantidade, id_filial):
        self._atualizar_estoque(id_produto, quantidade, id_filial)
        return True

    def registrar_venda(self, id_produto, quantidade, id_filial):
        if quantidade < 0:
            raise ValorInvalidoException("Quantidade não pode ser negativa para vendas")
        self._atualizar_estoque(id_produto, -quantidade, id_filial)
        return True

    def registrar_transferencia(self, id_filial_origem, id_filial_destino, id_produto, quantidade):
        if quantidade < 0:
            raise ValorInvalidoException("Quantidade não pode ser negativa para transferências")
        self._atualizar_estoque(id_produto, -quantidade, id_filial_origem)
        self._atualizar_estoque(id_produto, quantidade, id_filial_destino)
        return True

    def registrar_devolucao(self, id_produto, quantidade, id_filial):
        if quantidade < 0:
            raise ValorInvalidoException("Quantidade não pode ser negativa para devoluções")
        self._atualizar_estoque(id_produto, quantidade, id_filial)
        return True

    def registrar_ajuste(self, id_produto, quantidade, id_filial):
        if id_produto not in self.estoque or id_filial not in self.estoque[id_produto]:
            raise ValorInvalidoException("Produto ou filial não encontrados no estoque")

        novo_estoque = self.estoque[id_produto][id_filial] + quantidade
        if novo_estoque < 0:
            raise ValorInvalidoException("Estoque não pode ser negativo após ajuste")

        self.estoque[id_produto][id_filial] = novo_estoque
        return True

    def _atualizar_estoque(self, id_produto, quantidade, id_filial):
        if id_produto not in self.estoque or id_filial not in self.estoque[id_produto]:
            raise ValorInvalidoException("Produto ou filial não encontrados no estoque")

        self.estoque[id_produto][id_filial] += quantidade
        if self.estoque[id_produto][id_filial] < 0:
            raise ValorInvalidoException("Estoque não pode ser negativo após a atualização")

    def consultar_estoque(self, id_produto, id_filial):
        if id_produto in self.estoque and id_filial in self.estoque[id_produto]:
            return self.estoque[id_produto][id_filial]
        else:
            raise ValorInvalidoException("Produto ou filial não encontrados no estoque")
