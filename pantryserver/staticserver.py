from os import curdir, sep
import re
from http.server import HTTPServer

from baseserver import BaseWebServer


class StaticWebappServer(BaseWebServer):

    def do_GET(self):
        content_types = {
            '.html': 'text/html',
            '.htm':  'text/html',
            '.ico':  'image/x-icon',
            '.svg':  'image/svg+xml',
            '.css':  'text/css',
            '.js':   'application/javascript',
            '.json': 'application/json',
            '.map':  'application/x-navimap'
        }
        static_folder = 'webapp' + sep + 'build'
        file_extension_search = re.search('\\.[a-zA-Z]+$',
                                          self.path.split('?')[0])

        if '..' in self.path:
            self._send_illegal_path_part('..')
        elif '/.' in self.path:
            self._send_illegal_path_part('/.')
        elif '~' in self.path:
            self._send_illegal_path_part('~')
        elif file_extension_search \
                and file_extension_search.group(0) in content_types:
            self._set_headers(content_types[file_extension_search.group(0)])
            try:
                f = open(curdir + sep + static_folder + sep + self.path, 'rb')
                self.wfile.write(f.read())
                f.close()
            except IOError:
                self._send_not_found()
        elif '.' in self.path:
            # Request is probably for a file that is not an approved extension
            self._send_not_found()
        else:
            self._send_not_found()


