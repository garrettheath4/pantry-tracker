from string import Template
from http.server import HTTPServer

from .basehandler import BaseRequestHandler
from .statichandler import StaticFileRequestHandler
from .apihandler import ApiRequestHandler


class RequestRouter(BaseRequestHandler):

    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)

    # noinspection PyPep8Naming
    def do_GET(self):
        if str(self.path).startswith("/api"):
            ApiRequestHandler.do_GET(self)
        else:
            StaticFileRequestHandler.do_GET(self)
