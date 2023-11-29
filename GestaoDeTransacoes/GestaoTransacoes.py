class ValorInvalidoException(Exception):
    pass

class GerenciadorDeInventario:
    def registrar_venda(self, id_produto, quantidade):
        # Verificando se a quantidade é negativa
        if quantidade < 0:
            raise ValorInvalidoException("Quantidade não pode ser negativa")        
        return True
