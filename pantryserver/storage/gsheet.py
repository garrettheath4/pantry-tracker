from __future__ import print_function
from string import Template as TStr
import logging
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class GSheetInventory:

    NAME_PROP = "name"
    QUANTITY_PROP = "qty"
    UNIT_PROP = "unit"

    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    # The ID and range of a sample spreadsheet.
    # noinspection SpellCheckingInspection
    SPREADSHEET_ID = '1J3EZrysnfOrE6XVLJodydwPXQbHvYszzaZ67CFB9E5w'
    RANGE_NAME = 'At Work!A2:C'

    def __init__(self):
        """Shows basic usage of the Sheets API.
        Prints values from a sample spreadsheet.
        Source: https://developers.google.com/sheets/api/quickstart/python
        """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        # build(..) sends an API call
        service = build('sheets', 'v4', credentials=creds)
        self.data_fetcher = service.spreadsheets().values()

    def fetch_all_rows(self):
        # Call the Sheets API
        # .execute() sends an API call
        result = self.data_fetcher.get(spreadsheetId=self.SPREADSHEET_ID,
                                       range=self.RANGE_NAME).execute()
        return result.get('values', [])

    def fetch_all_items(self):
        items = {}
        values = self.fetch_all_rows()
        for [name, qty, unit] in values:
            items[name] = {}
            items[name][GSheetInventory.NAME_PROP] = name
            items[name][GSheetInventory.QUANTITY_PROP] = float(qty)
            items[name][GSheetInventory.UNIT_PROP] = unit
        return items

    def _find_indexed_item_row(self, item_name: str):
        values = self.fetch_all_rows()
        if not values:
            return None
        match_idx_rows = [(i, r) for i, r in enumerate(values)
                          if str(r[0]).lower().startswith(item_name.lower())]
        if not match_idx_rows:
            return None
        indexed_item_row = match_idx_rows[0]
        # item_index = 0..MAX_ROW_INDEX
        # item_row: item_name, item_quantity, item_quantity_unit
        if len(match_idx_rows) > 1:
            logging.warning("Found %d matches; only returning first: %s",
                            len(match_idx_rows), indexed_item_row)
        return indexed_item_row

    def find_item_row(self, item_name: str):
        index_item_row = self._find_indexed_item_row(item_name)
        if not index_item_row:
            return None
        (index, item_row) = index_item_row
        return item_row

    def contains_positive(self, item_name: str) -> bool:
        item_row = self.find_item_row(item_name)
        if not item_row:
            logging.warning("Item not found in sheet: %s", item_name)
            return False
        if len(item_row) < 2:
            logging.warning("Row does not contain at least three columns: %s",
                            item_row)
            return False
        [_, item_quantity, _] = item_row
        return float(item_quantity) > 0

    def __contains__(self, item):
        return self.contains_positive(item)

    def fetch_item_quantity(self, item_name: str) -> float:
        item_row = self.find_item_row(item_name)
        if not item_row:
            return 0.0
        if len(item_row) < 3:
            logging.warning("Row does not contain at least three columns: %s",
                            item_row)
            return 0.0
        [_, item_quantity, _] = item_row
        return float(item_quantity)

    def __getitem__(self, item):
        return self.fetch_item_quantity(item)

    def send_item_quantity(self, item_name: str, quantity: float):
        indexed_item_row = self._find_indexed_item_row(item_name)
        if not indexed_item_row:
            logging.warning("Item not found in Google Spreadsheet: %s",
                            item_name)
            return False
        (index, item_row) = indexed_item_row
        coord = "B" + str(index + 1 + 1)
        body = {
            "range": coord,
            "values": [[quantity]]
        }
        response = self.data_fetcher.update(spreadsheetId=self.SPREADSHEET_ID,
                                            range=coord, body=body,
                                            valueInputOption="RAW").execute()
        return response.get('updatedCells') == 1

    def __setitem__(self, key, value):
        self.send_item_quantity(str(key), float(value))

    def __str__(self):
        values = self.fetch_all_rows()
        lines = []
        for row in values:
            [name, qty, unit] = row
            lines.append(TStr("$item: $qty $unit")
                         .substitute(item=name, qty=qty, unit=unit))
        return "\n".join(lines)


if __name__ == "__main__":
    gs = GSheetInventory()
    print(gs)
    print()
    print(TStr("Bananas: $qty").substitute(qty=gs.fetch_item_quantity("Banana")))
    print(TStr("Tuna cans: $qty")
          .substitute(qty=gs.fetch_item_quantity("Tuna cans")))
    print(TStr("Nonexistent item: $qty")
          .substitute(qty=gs.fetch_item_quantity("Nonexistent item")))
    dairy_milk_name = "Dairy milk"
    orig_dairy_milk_qty = gs.fetch_item_quantity(dairy_milk_name)
    new_dairy_milk_qty = 9.9
    print(TStr("$name: $qty")
          .substitute(name=dairy_milk_name, qty=orig_dairy_milk_qty))
    print(TStr("Updating $name to $qty...")
          .substitute(name=dairy_milk_name, qty=new_dairy_milk_qty))
    gs.send_item_quantity("Dairy milk", new_dairy_milk_qty)
    print(TStr("$name: $qty")
          .substitute(name=dairy_milk_name,
                      qty=gs.fetch_item_quantity(dairy_milk_name)))
    print(TStr("Updating $name to $qty...")
          .substitute(name=dairy_milk_name, qty=orig_dairy_milk_qty))
    gs.send_item_quantity("Dairy milk", orig_dairy_milk_qty)
    print(TStr("$name: $qty")
          .substitute(name=dairy_milk_name,
                      qty=gs.fetch_item_quantity(dairy_milk_name)))
