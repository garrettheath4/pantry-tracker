from string import Template as TStr
from urllib.parse import urlparse, parse_qs

from .basehandler import BaseRequestHandler
from pantryserver.storage.inventory import Inventory

DEBUG = False


def log(message):
    if DEBUG:
        print(message)


class ApiRequestHandler(BaseRequestHandler):

    inventory = Inventory()

    # noinspection PyPep8Naming
    def do_GET(self):
        log(TStr("API call: $path").substitute(path=self.path))
        if not str(self.path).startswith("/api"):
            self._send_not_found()
        parsed = parse_qs(urlparse(self.path).query)
        log(TStr("Parsed query string: $parsed").substitute(parsed=parsed))
        if 'name' in parsed and 'count' in parsed:
            self.send_response(200)
            self.end_headers()
            itemName = parsed['name'][0]
            itemCount = parsed['count'][0]
            ApiRequestHandler.inventory.set(itemName, int(itemCount))
            log(TStr("Inventory: $items")
                .substitute(items=ApiRequestHandler.inventory))
            self.wfile.write(
                bytes(str(ApiRequestHandler.inventory.get(itemName)), "utf-8"))
        else:
            self._send_not_found()
