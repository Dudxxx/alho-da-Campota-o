from datetime import date


class Produto:
    def __init__(self, ean13, nome, descricao):
        self.ean13 = ean13
        self.nome = nome
        self.quantidade = 0
        self.validade = date.today()
        self.descricao = descricao
        self.precoUltimaCompra = 0.00
        self.dataFabricacao = date.today()
