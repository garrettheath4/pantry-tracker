import logging
from urllib.parse import urlparse, parse_qs

from .basehandler import BaseRequestHandler
from pantryserver.storage.inventory import Inventory
from pantryserver.storage.gsheet import GSheet


class ApiRequestHandler(BaseRequestHandler):

    inventory = Inventory(GSheet())

    # noinspection PyPep8Naming
    def do_GET(self):
        logging.debug("API call: %s", self.path)
        if not str(self.path).startswith("/api"):
            self._send_not_found()
        parsed = parse_qs(urlparse(self.path).query)
        if 'name' in parsed:
            itemName = parsed['name'][0]
            if 'count' in parsed:
                itemCount = float(parsed['count'][0])
                ApiRequestHandler.inventory.update(itemName, itemCount)
            else:
                itemCount = ApiRequestHandler.inventory.get(itemName)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(str(itemCount), "utf-8"))
        else:
            self._send_not_found()
