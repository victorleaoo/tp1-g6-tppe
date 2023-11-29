class ValorInvalidoException(Exception):
    pass

class GerenciadorDeInventario:
    def registrar_venda(self, id_produto, quantidade):
        # Verificando se a quantidade é negativa
        if quantidade < 0:
            raise ValorInvalidoException("Quantidade não pode ser negativa")        
        return True
        
    def registrar_transferencia(self, id_filial_origem, id_filial_destino, id_produto, quantidade):
        # Por enquanto, uma implementação básica para passar no teste
        if quantidade < 0:
            raise ValorInvalidoException("Quantidade não pode ser negativa")
        return True
