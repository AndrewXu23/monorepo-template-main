# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                if item.quality < 50:
                    item.quality += 2 if item.sell_in <= 0 else 1
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in <= 0:
                    item.quality = 0
                elif item.sell_in <= 5:
                    item.quality = min(item.quality + 3, 50)
                elif item.sell_in <= 10:
                    item.quality = min(item.quality + 2, 50)
                else:
                    item.quality = min(item.quality + 1, 50)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                pass  # Do nothing for Sulfuras
            elif item.name.startswith("Conjured"):
                if item.quality > 0:
                    item.quality -= 2 if item.sell_in > 0 else 4
                    item.quality = max(item.quality, 0)  # Ensure quality doesn't go negative
            else:
                if item.quality > 0:
                    item.quality -= 1 if item.sell_in > 0 else 2
                    item.quality = max(item.quality, 0)  # Ensure quality doesn't go negative
            
            # Decrease sell_in for all items except Sulfuras
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1
