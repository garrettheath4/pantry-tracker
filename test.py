import unittest

from pantryserver.storage.inventory import Inventory
from pantryserver.storage.gsheet import GSheet


class TestGSheet(unittest.TestCase):

    # noinspection SpellCheckingInspection
    def test_gsheet_peanut_butter_pos(self):
        gs = GSheet()
        self.assertTrue(gs.contains_positive("Peanut butter"))

    # noinspection SpellCheckingInspection
    def test_gsheet_nonexist_item(self):
        gs = GSheet()
        self.assertEqual(gs.fetch_item_quantity("Nonexistent item"), 0.0)


class TestDictInventory(unittest.TestCase):

    def test_dict_get_update(self):
        item_name = "Milk"
        item_quantity = 1.8
        inv = Inventory()
        self.assertEqual(inv.get(item_name), 0.0)
        inv.update(item_name, item_quantity)
        self.assertEqual(inv.get(item_name), item_quantity)

    def test_contains_positive(self):
        item_name = "Milk"
        item_quantity = 1.8
        inv = Inventory()
        inv.update(item_name, item_quantity)
        self.assertTrue(inv.contains_positive(item_name))


if __name__ == '__main__':
    unittest.main()
