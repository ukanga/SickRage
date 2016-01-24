import logging
import putio
from .generic import GenericClient


class PutioApi(GenericClient):
    def __init__(self, host=None, username=None, password=None):

        super(PutioApi, self).__init__('Putio', host, username, password)

        self.auth = self.password
        self.client = putio.Client(self.auth)
        self.parent_id = 0
        self.putio_folder = 'TV Shows'

    def _get_auth(self):
        return self.auth

    def _get_putio_folder_id(self, folder):
        for f in self.client.File.list():
            if f.name == folder:
                return f.id

        return self.parent_id

    def _get_transfer_by_uri(self, uri):
        for transfer in self.client.Transfer.list():
            if transfer.magneturi == uri:
                return transfer

        return None

    def _add_torrent_uri(self, result):
        parent_id = self._get_putio_folder_id(self.putio_folder)
        transfer = self._get_transfer_by_uri(result.url)
        url = result.url

        if transfer is None:
            transfer = self.client.Transfer.add_url(url, parent_id)
            logging.debug(
                self.name + u': added ' + transfer.name +
                ' [' + str(transfer.id) + ']'
            )

        return transfer.id

    def testAuthentication(self):
        try:
            file_list = self.client.File.list()
            if len(file_list):
                return True, 'Success: Connected and Authenticated'
            else:
                return False, 'Error: Unable to get ' + self.name \
                    + ' Authentication, check your config!'

        except Exception:
            return False, 'Error: Unable to connect to ' + self.name


api = PutioApi()
