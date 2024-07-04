# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class abstract_class(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def update(self):
        pass


class ItemBase(abstract_class):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    @abstractmethod
    def update(self):
        pass


class AgedBrie(ItemBase):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update(self):
        if self.quality < 50:
            self.quality += 1

        self.sell_in -= 1
        if self.sell_in < 0 and self.quality < 50:
            self.quality += 1


class Sulfuras(ItemBase):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update(self):
        if self.quality < 50:
            self.quality += 1


class Backstage_Passes(ItemBase):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update(self):
        if self.quality < 50:
            self.quality += 1
            if self.sell_in < 11:
                self.quality += 1
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality = 0


class Noname(ItemBase):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update(self):
        if self.quality > 0:
            self.quality -= 1
        self.sell_in -= 1

        if self.sell_in >= 0 or self.quality > 0:
            self.quality -= 1


class GildedRose(object):
    def __init__(self, items: abstract_class):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update()
