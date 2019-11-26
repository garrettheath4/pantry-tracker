import re
from os import curdir, sep
import logging

from .basehandler import BaseRequestHandler


class StaticFileRequestHandler(BaseRequestHandler):

    static_folder = 'webapp' + sep + 'build'
    content_types = {
        '.html': 'text/html',
        '.htm': 'text/html',
        '.ico': 'image/x-icon',
        '.png': 'image/png',
        '.svg': 'image/svg+xml',
        '.css': 'text/css',
        '.js': 'application/javascript',
        '.json': 'application/json',
        '.map': 'application/x-navimap',
    }

    # noinspection PyPep8Naming
    def do_GET(self):
        file_extension_search = re.search('\\.[a-zA-Z]+$',
                                          self.path.split('?')[0])

        if '..' in self.path:
            self._send_illegal_path_part('..')
        elif '/.' in self.path:
            self._send_illegal_path_part('/.')
        elif '~' in self.path:
            self._send_illegal_path_part('~')
        elif (file_extension_search and file_extension_search.group(0)
                in StaticFileRequestHandler.content_types) or self.path == '/':
            if self.path == '/':
                file_path = 'index.html'
                content_type = 'text/html'
            else:
                file_path = self.path
                content_type = StaticFileRequestHandler.content_types[
                    file_extension_search.group(0)]
            try:
                f = open(curdir + sep + StaticFileRequestHandler.static_folder
                         + sep + file_path, 'rb')
                self._set_headers(content_type)
                self.wfile.write(f.read())
                f.close()
            except IOError:
                self._send_not_found()
        elif '.' in self.path:
            logging.warning("Path does not have an approved extension - %s", self.path)
            self._send_not_found()
        else:
            self._send_not_found()
