class Fornecedor:
    def __init__(self, id, nome, endereco, data_contrato):
        self.validar_id(id)
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.data_contrato = data_contrato
    
    @staticmethod
    def validar_id(id):
        if id is None or id is '':
            raise ValueError("ID não pode ser nulo")
        if isinstance(id, str):
            raise ValueError("ID não pode ser uma string")
