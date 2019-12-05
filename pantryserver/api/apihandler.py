import logging
from urllib.parse import urlparse, parse_qs
import subprocess

from .basehandler import BaseRequestHandler
from pantryserver.storage.inventory import Inventory
from pantryserver.storage.gsheet import GSheet


class ApiRequestHandler(BaseRequestHandler):

    inventory = Inventory(GSheet())

    # noinspection PyPep8Naming
    def do_GET(self):
        path = str(self.path)
        logging.debug("API call: %s", path)
        if not path.startswith("/api"):
            self._send_not_found()
        if path.startswith("/api/item"):
            itemQuery = parse_qs(urlparse(self.path).query)
            if 'name' in itemQuery:
                itemName = itemQuery['name'][0]
                if 'count' in itemQuery:
                    itemCount = float(itemQuery['count'][0])
                    ApiRequestHandler.inventory.update(itemName, itemCount)
                else:
                    itemCount = ApiRequestHandler.inventory.get(itemName)
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(str(itemCount), "utf-8"))
            else:
                self._send_not_found()
        elif path.startswith("/api/app/update"):
            logging.info("Received API request to update app: GET /api/app/update")
            updateCommand = "git pull && cd webapp && npm run build"
            updateQuery = parse_qs(urlparse(self.path).query)
            if 'blocking' in updateQuery \
                    and str(updateQuery['blocking'][0]).lower() \
                    in ['true', '1', 'yes']:
                process = subprocess.run(updateCommand.split(),
                                         capture_output=True,
                                         text=True,
                                         check=True,
                                         timeout=120)
                logging.info("Update complete. Responding to request with OK.")
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes("OK updated app", "utf-8"))
            else:
                process = subprocess.Popen(updateCommand.split(),
                                           stdout=subprocess.PIPE)
                logging.info("Updating app. Responding to request with OK now.")
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes("OK updating app", "utf-8"))
        elif path.startswith("/api/system/restart"):
            logging.warning("Received API request to restart system: GET /api/system/restart")
            rebootCommand = "sudo reboot"
            process = subprocess.run(rebootCommand.split(),
                                     capture_output=True,
                                     text=True,
                                     check=True)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes("OK restarting system", "utf-8"))
        else:
            self._send_not_found()
