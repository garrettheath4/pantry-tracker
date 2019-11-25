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
        logging.debug("Parsed query string: %s", parsed)
        if 'name' in parsed and 'count' in parsed:
            self.send_response(200)
            self.end_headers()
            itemName = parsed['name'][0]
            itemCount = parsed['count'][0]
            ApiRequestHandler.inventory.update(itemName, int(itemCount))
            self.wfile.write(
                bytes(str(ApiRequestHandler.inventory.get(itemName)), "utf-8"))
        else:
            self._send_not_found()
