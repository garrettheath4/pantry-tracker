from string import Template
from http.server import BaseHTTPRequestHandler, HTTPServer


class BaseRequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self, content_type='text/html'):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def _send_not_found(self):
        t = Template("$path does not exist")
        self.send_error(404, "File Not Found", t.substitute(path=self.path))

    def _send_not_implemented(self):
        self.send_error(501, "Not Implemented",
                        "Please override the GET method in this BaseWebServer"
                        " class")

    def _send_illegal_path_part(self, invalid_substring=""):
        error_template = Template("Path requested contains illegal$sub substring - $path")
        maybe_sub = Template(" '$inside'").substitute(inside=invalid_substring) if invalid_substring else ""
        error_message = error_template.substitute(sub=maybe_sub, path=self.path)
        self.send_error(403, "Illegal Path", error_message)

    # noinspection PyPep8Naming
    def do_HEAD(self):
        self._set_headers()

    # noinspection PyPep8Naming
    def do_GET(self):
        self._send_not_implemented()


def run(server_class=HTTPServer, handler_class=BaseRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(Template("Starting httpd on port $port ...").substitute(port=port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("^C received, shutting down server")
        httpd.socket.close()
