import unittest

from gilded_rose import Item, GildedRose

class MyTestCase(unittest.TestCase):
    # Testa o comportamento de um item genérico
    def test_item(self):
        valor_teste: int = 5
        valor_teste_negativo = -valor_teste
        items = [
            Item("item_positivo", valor_teste, valor_teste),
            Item("item_quality_negativa", valor_teste, valor_teste_negativo),
            Item("item_sell_in_negativo", valor_teste_negativo, valor_teste),
            Item("item_negativo", valor_teste_negativo, valor_teste_negativo),
            Item("item_zerado", 0, 0),
            Item("item_overflow_quality", valor_teste, 100),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        # Verifica a atualização de um item com valores positivos
        self.assertEqual("item_positivo", items[0].name)
        self.assertEqual(valor_teste - 1, items[0].sell_in)
        self.assertEqual(valor_teste - 1, items[0].quality)

        # Verifica se a qualidade negativa é limitada a zero
        self.assertEqual("item_quality_negativa", items[1].name)
        self.assertEqual(valor_teste - 1, items[1].sell_in)
        self.assertEqual(0, items[1].quality)

        # Verifica a redução da qualidade de um item com prazo de validade expirado
        self.assertEqual("item_sell_in_negativo", items[2].name)
        self.assertEqual(valor_teste_negativo - 1, items[2].sell_in)
        self.assertEqual(valor_teste - 2, items[2].quality)

        # Verifica o comportamento de um item com valores negativos
        self.assertEqual("item_negativo", items[3].name)
        self.assertEqual(valor_teste_negativo - 1, items[3].sell_in)
        self.assertEqual(0, items[3].quality)

        # Verifica o comportamento de um item com valores zerados
        self.assertEqual("item_zerado", items[4].name)
        self.assertEqual(-1, items[4].sell_in)
        self.assertEqual(0, items[4].quality)

        # Verifica o limite máximo de qualidade permitido para um item
        self.assertEqual("item_overflow_quality", items[5].name)
        self.assertEqual(valor_teste - 1, items[5].sell_in)
        self.assertEqual(50, items[5].quality)


if __name__ == '__main__':
    unittest.main()
