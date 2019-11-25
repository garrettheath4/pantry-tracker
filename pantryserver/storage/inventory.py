import logging


class Inventory:

    def __init__(self, items=None):
        if items is None:
            items = dict()
        self.items = items

    def contains_positive(self, item_name: str):
        return item_name in self.items and self.items[item_name] > 0

    def get(self, item_name: str) -> float:
        if item_name in self.items:
            return self.items[item_name]
        else:
            logging.debug("Item '%s' does not exist in inventory; reporting 0"
                          " inventory", item_name)
            return 0.0

    def update(self, item_name: str, quantity: float):
        if item_name not in self.items:
            logging.info("Creating item %s with %1.1f items", item_name, quantity)
        self.items[item_name] = max(float(quantity), 0.0)
        if self.items[item_name] <= 0.0:
            if quantity == 0.0:
                logging.info("Item now has 0 inventory for %s", item_name)
            else:
                logging.warning("Item now has 0 inventory for %s (tried to set"
                                " to %1.1f)", item_name, quantity)

    def increment(self, item_name: str):
        if item_name in self.items:
            self.items[item_name] = max(self.items[item_name], 0.0) + 1
        else:
            self.items[item_name] = 1
        return self.items[item_name]

    def decrement(self, item_name: str):
        if item_name in self.items:
            self.items[item_name] = max(self.items[item_name] - 1.0, 0.0)
        else:
            self.items[item_name] = 0.0
        return self.items[item_name]

    def __str__(self):
        return str(self.items)
