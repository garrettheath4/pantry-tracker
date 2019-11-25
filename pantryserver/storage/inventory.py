from string import Template as TStr

DEBUG = True


def log(message):
    if DEBUG:
        print(message)


class Inventory:

    def __init__(self, items=None):
        if items is None:
            items = dict()
        self.items = items

    def contains_positive(self, item_name):
        return item_name in self.items and self.items[item_name] > 0

    def get(self, item):
        if item in self.items:
            return self.items[item]
        else:
            log(TStr("Item '$item' does not exist in inventory; reporting 0"
                     " inventory").substitute(item=item))
            return 0

    def set(self, item, quantity):
        if DEBUG and item not in self.items:
            log(TStr("Creating item $item with $count items")
                .substitute(item=item, count=quantity))
        self.items[item] = max(int(quantity), 0)
        if self.items[item] <= 0:
            log(TStr("Item now has 0 inventory for $item")
                .substitute(item=item))
            if quantity != 0:
                log(TStr("(tried to set to $quantity)")
                    .substitute(quantity=quantity))

    def increment(self, item):
        if item in self.items:
            self.items[item] = max(self.items[item], 0) + 1
        else:
            self.items[item] = 1
        return self.items[item]

    def decrement(self, item):
        if item in self.items:
            self.items[item] = max(self.items[item] - 1, 0)
        else:
            self.items[item] = 0
        return self.items[item]

    def __str__(self):
        return str(self.items)
