from os import curdir, sep
import re

from .basehandler import BaseRequestHandler


class StaticFileRequestHandler(BaseRequestHandler):

    # noinspection PyPep8Naming
    def do_GET(self):
        content_types = {
            '.html': 'text/html',
            '.htm':  'text/html',
            '.ico':  'image/x-icon',
            '.png':  'image/png',
            '.svg':  'image/svg+xml',
            '.css':  'text/css',
            '.js':   'application/javascript',
            '.json': 'application/json',
            '.map':  'application/x-navimap',
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
            print("Path does not have an approved extension - %s" % self.path)
            self._send_not_found()
        else:
            self._send_not_found()
