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

    def contains_positive(self, item_name: str):
        return item_name in self.items and self.items[item_name] > 0

    def get(self, item_name: str):
        if item_name in self.items:
            return self.items[item_name]
        else:
            log(TStr("Item '$item' does not exist in inventory; reporting 0"
                     " inventory").substitute(item=item_name))
            return 0

    def update(self, item_name: str, quantity: float):
        if DEBUG and item_name not in self.items:
            log(TStr("Creating item $item with $count items")
                .substitute(item=item_name, count=quantity))
        self.items[item_name] = max(float(quantity), 0.0)
        if self.items[item_name] <= 0:
            log(TStr("Item now has 0 inventory for $item")
                .substitute(item=item_name))
            if quantity != 0.0:
                log(TStr("(tried to set to $quantity)")
                    .substitute(quantity=quantity))

    def increment(self, item_name: str):
        if item_name in self.items:
            self.items[item_name] = max(self.items[item_name], 0) + 1
        else:
            self.items[item_name] = 1
        return self.items[item_name]

    def decrement(self, item_name: str):
        if item_name in self.items:
            self.items[item_name] = max(self.items[item_name] - 1, 0)
        else:
            self.items[item_name] = 0
        return self.items[item_name]

    def __str__(self):
        return str(self.items)
