import unittest

from gilded_rose import Item, GildedRose

class MyTestCase(unittest.TestCase):
    # Testa o comportamento de um item genérico
    def test_sulfuras(self):
        valor_teste: int = 80
        valor_teste_negativo = -valor_teste
        items = [
            Item("Sulfuras, Hand of Ragnaros", 0, 0),
            Item("Sulfuras, Hand of Ragnaros", valor_teste, 0),
            Item("Sulfuras, Hand of Ragnaros", valor_teste, valor_teste),
            Item("Sulfuras, Hand of Ragnaros", 0, valor_teste)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        # Verifica a atualização de um item com valores positivos
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

        # Verifica a atualização de um item com valores positivos
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[1].name)
        self.assertEqual(valor_teste, items[1].sell_in)
        self.assertEqual(0, items[1].quality)

        # Verifica a atualização de um item com valores positivos
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[2].name)
        self.assertEqual(valor_teste, items[2].sell_in)
        self.assertEqual(valor_teste, items[2].quality)

        # Verifica a atualização de um item com valores positivos
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[3].name)
        self.assertEqual(0, items[3].sell_in)
        self.assertEqual(valor_teste, items[3].quality)

if __name__ == '__main__':
    unittest.main()
