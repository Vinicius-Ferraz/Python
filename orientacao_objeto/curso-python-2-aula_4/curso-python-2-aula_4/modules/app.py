from restaurante import Restaurante
from cardapio.prato import Prato
from cardapio.bebida import Bebida



restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de melancia', 5.0, 'grande')
prato_pao = Prato('Pãozinho', 2.00,'O melhor pão da cidade')
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)


def main():
    restaurante_praca.exibir_cardapio()


if __name__ == '__main__':
    main()

