# -*- coding: utf-8 -*-
#Se simplico las llamadas a estos textos
A = "Aged Brie"
B = "Backstage passes to a TAFKAL80ETC concert"
S = "Sulfuras, Hand of Ragnaros"

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.quality < 50 and item.name != S:
                if item.sellIn > 0 and item.quality <= 49:
                    item.quality += 1
                    if item.name == B and item.sellIn<=10 and item.quality <= 49:
                        item.quality +=1
                        if item.sellIn <= 5 and item.quality <= 49:
                            item.quality +=1
                elif item.sellIn < 0:
                    if item.name == B:
                        item.quality = 0
                    else:
                        item.quality +=2
                item.sellIn -= 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
