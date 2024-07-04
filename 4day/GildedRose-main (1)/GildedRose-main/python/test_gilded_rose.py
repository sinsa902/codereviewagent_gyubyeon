# -*- coding: utf-8 -*-
import unittest
from typing import List, Any

from gilded_rose import *

SULFURAS = "Sulfuras, Hand of Ragnaros"

NONAME = "noname"
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Noname("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_empty_item(self):
        items: list[Any] = []
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(0, len(items))

    def test_noname_0_0(self):
        items = [Noname(NONAME, 0, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_noname_0_1(self):
        items = [Noname(NONAME, 0, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_noname_2_0(self):
        items = [Noname(NONAME, 0, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_sulfuras_sellin_0_80(self):
        items = [Sulfuras(SULFURAS, 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_aged_brie_sellin_0_0(self):
        items = [AgedBrie(AGED_BRIE, 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_backstage_pass_sellin_0_0(self):
        items = [Backstage_Passes(BACKSTAGE_PASS, 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_backstage_pass_sellin_12_0(self):
        items = [Backstage_Passes(BACKSTAGE_PASS, 12, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_Sulfuras_2_80(self):
        items = [Sulfuras(SULFURAS, -2, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(80, items[0].quality)


if __name__ == "__main__":
    unittest.main()
