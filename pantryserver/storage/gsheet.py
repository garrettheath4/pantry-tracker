from __future__ import print_function
from string import Template as TStr
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

DEBUG = True


def log(message):
    if DEBUG:
        print(message)


class GSheet:

    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    # The ID and range of a sample spreadsheet.
    # noinspection SpellCheckingInspection
    SPREADSHEET_ID = '1J3EZrysnfOrE6XVLJodydwPXQbHvYszzaZ67CFB9E5w'
    RANGE_NAME = 'At Work!A2:C50'

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

    def _find_indexed_item_row(self, item_name: str):
        values = self.fetch_all_rows()
        if not values:
            return None
        match_idx_rows = [(i, r) for i, r in enumerate(values)
                          if str(r[0]).lower().startswith(item_name.lower())]
        if not match_idx_rows:
            log(TStr("Item not found in sheet: $item")
                .substitute(item=item_name))
            return None
        indexed_item_row = match_idx_rows[0]
        # item_index = 0..MAX_ROW_INDEX
        # item_row: item_name, item_quantity, item_quantity_unit
        if len(match_idx_rows) > 1:
            log(TStr("Found $qty matches in sheet; only returning first: $one")
                .substitute(qty=len(match_idx_rows), one=indexed_item_row))
        return indexed_item_row

    def find_item_row(self, item_name: str):
        index_item_row = self._find_indexed_item_row(item_name)
        if not index_item_row:
            return None
        index, item_row = index_item_row
        return item_row

    def contains_positive(self, item_name: str) -> bool:
        item_row = self.find_item_row(item_name)
        if not item_row:
            log(TStr("Item not found in sheet: $item")
                .substitute(item=item_name))
            return False
        if len(item_row) < 2:
            log(TStr("Row does not contain at least three columns: $row")
                .substitute(row=item_row))
            return False
        _, item_quantity, _ = item_row
        return float(item_quantity) > 0

    def __contains__(self, item):
        return self.contains_positive(item)

    def fetch_item_quantity(self, item_name: str) -> float:
        item_row = self.find_item_row(item_name)
        if not item_row:
            return 0.0
        if len(item_row) < 3:
            log(TStr("Row does not contain at least three columns: $row")
                .substitute(row=item_row))
            return 0.0
        _, item_quantity, _ = item_row
        return float(item_quantity)

    def __getitem__(self, item):
        return self.fetch_item_quantity(item)

    def send_item_quantity(self, item_name: str, quantity: float):
        # TODO
        indexed_item_row = self._find_indexed_item_row(item_name)
        if not indexed_item_row:
            return False
        index, item_row = indexed_item_row


    def __str__(self):
        values = self.fetch_all_rows()
        lines = []
        for row in values:
            # Print columns A and B, which correspond to indices 0 and 1.
            lines.append(TStr("$item: $qty $unit")
                         .substitute(item=row[0], qty=row[1], unit=row[2]))
        return "\n".join(lines)


if __name__ == "__main__":
    gs = GSheet()
    print(gs)
    print()
    print(TStr("Bananas: $qty").substitute(qty=gs.fetch_item_quantity("Banana")))
