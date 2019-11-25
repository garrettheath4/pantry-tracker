import unittest

from pantryserver.storage.gsheet import GSheet


class TestPantryServer(unittest.TestCase):

    # noinspection SpellCheckingInspection
    def test_gsheet_peanut_butter_pos(self):
        gs = GSheet()
        self.assertTrue(gs.contains_positive("Peanut butter"))


if __name__ == '__main__':
    unittest.main()
