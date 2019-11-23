from string import Template
from urllib.parse import urlparse, parse_qs

from .basehandler import BaseRequestHandler

items = {
    'apples': 5,
    'bananas': 5,
}


class ApiRequestHandler(BaseRequestHandler):

    # noinspection PyPep8Naming
    def do_GET(self):
        print(Template("API call: $path").substitute(path=self.path))
        if not str(self.path).startswith("/api"):
            self._send_not_found()
        parsed = parse_qs(urlparse(self.path).query)
        # print(Template("Parsed query string: $parsed").substitute(parsed=parsed))
        if 'name' in parsed and 'count' in parsed:
            self.send_response(200)
            self.end_headers()
            items[parsed['name'][0]] = int(parsed['count'][0])
            print(Template("Items: $items").substitute(items=items))
            self.wfile.write(bytes(str(items[parsed['name'][0]]), "utf-8"))
        else:
            self._send_not_found()
