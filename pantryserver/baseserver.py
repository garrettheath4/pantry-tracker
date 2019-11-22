from http.server import BaseHTTPRequestHandler, HTTPServer


class BaseWebServer(BaseHTTPRequestHandler):

    def _set_headers(self, content_type='text/html'):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def _send_not_found(self):
        self.send_error(404, "File Not Found", "%s does not exist" % self.path)

    def _send_not_implemented(self):
        self.send_error(501, "Not Implemented",
                        "Please override the GET method in this BaseWebServer"
                        " class")

    def _send_illegal_path_part(self, invalid_substring=""):
        error_message = "Path requested contains illegal%s substring - %s" \
                        % (" '%s'" % invalid_substring if invalid_substring
                           else "",
                           self.path)
        self.send_error(403, "Illegal Path", error_message)

    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        self._send_not_implemented()


def run(server_class=HTTPServer, handler_class=BaseWebServer, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port %s ...' % port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("^C received, shutting down server")
        httpd.socket.close()
