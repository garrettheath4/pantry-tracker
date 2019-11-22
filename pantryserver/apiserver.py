from baseserver import BaseWebServer


class PantryApiServer(BaseWebServer):

    def do_GET(self):
        if not str(self.path).startswith("/api"):
            self._send_not_found()
