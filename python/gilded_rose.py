# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            item.sell_in = item.sell_in - 1

            match item.name:
                case "Backstage passes to a TAFKAL80ETC concert":
                    if 50 > item.quality > 0:
                        if item.sell_in < 0:
                            item.quality = 0
                        elif item.sell_in <= 5:
                            item.quality = item.quality + 3
                        elif item.sell_in <= 10:
                            item.quality = item.quality + 2
                        else:
                            item.quality = item.quality + 1
                case "Aged Brie":
                    if item.sell_in < 0:
                        item.quality = item.quality + 2
                    else:
                        item.quality = item.quality + 1

                case "Conjured Mana Cake":
                    if item.sell_in >= 0:
                        item.quality = item.quality - 2
                    else:
                        item.quality = item.quality - 4
                case _:
                    if item.sell_in < 0:
                        item.quality = item.quality - 2
                    else:
                        item.quality = item.quality - 1

            if item.quality > 50:
                item.quality = 50
            elif item.quality < 0:
                item.quality = 0


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
