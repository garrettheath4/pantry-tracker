import unittest

from pantryserver.storage.inventory import Inventory
from pantryserver.storage.gsheet import GSheetInventory


class TestGSheetBase(unittest.TestCase):

    # noinspection SpellCheckingInspection
    def test_gsheet_peanut_butter_pos(self):
        gs = GSheetInventory()
        self.assertTrue(gs.contains_positive("Peanut butter"))

    # noinspection SpellCheckingInspection
    def test_gsheet_nonexist_item(self):
        gs = GSheetInventory()
        self.assertEqual(gs.fetch_item_quantity("Nonexistent item"), 0.0)

    # noinspection SpellCheckingInspection
    def test_gsheet_fetch_all_rows(self):
        gs = GSheetInventory()
        rows = gs.fetch_all_rows()
        self.assertNotEqual(len(rows), 0)

    # noinspection SpellCheckingInspection
    def test_gsheet_fetch_all_items(self):
        gs = GSheetInventory()
        items = gs.fetch_all_items()
        self.assertNotEqual(len(items), 0)
        self.assertEqual(items["Peanut butter"]["name"], "Peanut butter")
        self.assertNotEqual(items["Peanut butter"]["qty"], 0.0)
        self.assertEqual(items["Peanut butter"]["unit"], "bottles (16 oz)")

    # noinspection SpellCheckingInspection
    def test_gsheet_find_item_row(self):
        gs = GSheetInventory()
        item = gs.find_item_row("Peanut butter")
        self.assertNotEqual(item, None)


class TestDictInventory(unittest.TestCase):

    def test_dict_get_update(self):
        item_name = "Milk"
        item_quantity = 1.8
        inv = Inventory()
        self.assertEqual(inv.source, "dict")
        self.assertEqual(inv.get(item_name), 0.0)
        inv.update(item_name, item_quantity)
        self.assertEqual(inv.get(item_name), item_quantity)

    def test_contains_positive(self):
        item_name = "Milk"
        item_quantity = 1.8
        inv = Inventory()
        inv.update(item_name, item_quantity)
        self.assertTrue(inv.contains_positive(item_name))


class TestGSheetInventory(unittest.TestCase):

    # noinspection SpellCheckingInspection
    def test_gsheet_get(self):
        item_name = "Peanut butter"
        inv = Inventory(GSheetInventory())
        self.assertEqual(inv.source, "GSheetInventory")
        self.assertGreater(inv.get(item_name), 0.0)
        self.assertTrue(inv.contains_positive(item_name))


if __name__ == '__main__':
    unittest.main()
