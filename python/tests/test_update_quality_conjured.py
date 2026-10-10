import unittest

from gilded_rose import Item, GildedRose

class MyTestCase(unittest.TestCase):
    # Testa o comportamento de itens Conjured (decaem o dobro da taxa normal)
    def test_conjured(self):
        valor_teste: int = 6
        valor_teste_negativo = -valor_teste
        items = [
            Item("Conjured Mana Cake", valor_teste, valor_teste),
            Item("Conjured Mana Cake", valor_teste, 1),
            Item("Conjured Mana Cake", valor_teste_negativo, valor_teste),
            Item("Conjured Mana Cake", 0, valor_teste),
            Item("Conjured Mana Cake", valor_teste, 100),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        # Verifica decaimento normal em dobro (sell_in > 0): -2 quality
        self.assertEqual("Conjured Mana Cake", items[0].name)
        self.assertEqual(valor_teste - 1, items[0].sell_in)
        self.assertEqual(valor_teste - 2, items[0].quality)

        # Verifica se qualidade não fica abaixo de zero
        self.assertEqual("Conjured Mana Cake", items[1].name)
        self.assertEqual(valor_teste - 1, items[1].sell_in)
        self.assertEqual(0, items[1].quality)

        # Verifica decaimento em dobro após prazo de validade (sell_in < 0): -4 quality
        self.assertEqual("Conjured Mana Cake", items[2].name)
        self.assertEqual(valor_teste_negativo - 1, items[2].sell_in)
        self.assertEqual(valor_teste - 4, items[2].quality)

        # Verifica sell_in zero (torna-se -1, decaimento -4)
        self.assertEqual("Conjured Mana Cake", items[3].name)
        self.assertEqual(-1, items[3].sell_in)
        self.assertEqual(valor_teste - 4, items[3].quality)

        # Verifica limite máximo de qualidade (overflow 100 -> 50)
        self.assertEqual("Conjured Mana Cake", items[4].name)
        self.assertEqual(valor_teste - 1, items[4].sell_in)
        self.assertEqual(50, items[4].quality)

if __name__ == '__main__':
    unittest.main()
