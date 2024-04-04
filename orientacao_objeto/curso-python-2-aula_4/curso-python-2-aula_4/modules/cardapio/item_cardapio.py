from abc import ABC, abstractmethod

class ItemCardapio:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco


    @abstractmethod
    def aplicar_desconto(self):
        pass
    #
    # def __str__(self):
    #     return f'{self.nome} | {self.preco}'

