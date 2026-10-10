import unittest

from gilded_rose import Item, GildedRose

class MyTestCase(unittest.TestCase):

    def test_backstage_passes(self):
        valor_teste: int = 5
        valor_teste_negativo = -valor_teste
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 15, valor_teste),
            Item("Backstage passes to a TAFKAL80ETC concert", 10, valor_teste),
            Item("Backstage passes to a TAFKAL80ETC concert", 5, valor_teste),
            Item("Backstage passes to a TAFKAL80ETC concert", 0, valor_teste),
            Item("Backstage passes to a TAFKAL80ETC concert", valor_teste_negativo, valor_teste),
            Item("Backstage passes to a TAFKAL80ETC concert", 5, 49),
            Item("Backstage passes to a TAFKAL80ETC concert", 10, 49),
            Item("Backstage passes to a TAFKAL80ETC concert", 15, 50),
            Item("Backstage passes to a TAFKAL80ETC concert", 5, 0),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        # Verifica sell_in > 10 (aumento de 1)
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(valor_teste + 1, items[0].quality)

        # Verifica 6 <= sell_in <= 10 (aumento de 2)
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[1].name)
        self.assertEqual(9, items[1].sell_in)
        self.assertEqual(valor_teste + 2, items[1].quality)

        # Verifica 1 <= sell_in <= 5 (aumento de 3)
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[2].name)
        self.assertEqual(4, items[2].sell_in)
        self.assertEqual(valor_teste + 3, items[2].quality)

        # Verifica sell_in <= 0 (qualidade cai para 0)
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[3].name)
        self.assertEqual(-1, items[3].sell_in)
        self.assertEqual(0, items[3].quality)

        # Verifica comportamento com sell_in negativo
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[4].name)
        self.assertEqual(valor_teste_negativo - 1, items[4].sell_in)
        self.assertEqual(0, items[4].quality)

        # Verifica limite máximo de qualidade 50 (sell_in = 5)
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[5].name)
        self.assertEqual(4, items[5].sell_in)
        self.assertEqual(50, items[5].quality)

        # Verifica limite máximo de qualidade 50 (sell_in = 10)
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[6].name)
        self.assertEqual(9, items[6].sell_in)
        self.assertEqual(50, items[6].quality)

        # Verifica limite máximo de qualidade 50 (sell_in = 15)
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[7].name)
        self.assertEqual(14, items[7].sell_in)
        self.assertEqual(50, items[7].quality)

        # Verifica qualidade inicial zero
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[8].name)
        self.assertEqual(4, items[8].sell_in)
        self.assertEqual(0, items[8].quality)

if __name__ == '__main__':
    unittest.main()
