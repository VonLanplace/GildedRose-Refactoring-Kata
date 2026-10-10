import unittest

from gilded_rose import Item, GildedRose

class MyTestCase(unittest.TestCase):

    def test_aged_brie(self):
        valor_teste: int = 5
        valor_teste_negativo = -valor_teste
        items = [
            Item("Aged Brie", valor_teste, valor_teste),
            Item("Aged Brie", valor_teste_negativo, valor_teste),
            Item("Aged Brie", valor_teste, valor_teste_negativo),
            Item("Aged Brie", valor_teste_negativo, valor_teste_negativo),
            Item("Aged Brie", 0, 0),
            Item("Aged Brie", valor_teste, 100),
            Item("Aged Brie", valor_teste, 50)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        # Verifica a atualização de um item com valores positivos
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(valor_teste - 1, items[0].sell_in)
        self.assertEqual(valor_teste + 1, items[0].quality)

        # Verifica se a qualidade negativa é limitada a zero
        self.assertEqual("Aged Brie", items[1].name)
        self.assertEqual(valor_teste_negativo - 1, items[1].sell_in)
        self.assertEqual(valor_teste + 2 , items[1].quality)

        # Verifica a redução da qualidade de um item com prazo de validade expirado
        self.assertEqual("Aged Brie", items[2].name)
        self.assertEqual(valor_teste - 1, items[2].sell_in)
        self.assertEqual(0 , items[2].quality)

        # Verifica o comportamento de um item com valores negativos
        self.assertEqual("Aged Brie", items[3].name)
        self.assertEqual(valor_teste_negativo - 1, items[3].sell_in)
        self.assertEqual(0 , items[3].quality)

        # Verifica o comportamento de um item com valores zerados
        self.assertEqual("Aged Brie", items[4].name)
        self.assertEqual(-1, items[4].sell_in)
        self.assertEqual(+2, items[4].quality)

        # Verifica o limite máximo de qualidade permitido para um item
        self.assertEqual("Aged Brie", items[5].name)
        self.assertEqual(valor_teste - 1, items[5].sell_in)
        self.assertEqual(50, items[5].quality)

        # Verifica o limite máximo de qualidade permitido para um item
        self.assertEqual("Aged Brie", items[5].name)
        self.assertEqual(valor_teste - 1, items[5].sell_in)
        self.assertEqual(50, items[5].quality)

if __name__ == '__main__':
    unittest.main()
