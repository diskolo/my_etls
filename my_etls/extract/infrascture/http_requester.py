import requests

from my_etls.extract.domain.requester import Requester


class HttpRequester(Requester):
    def get(self, url):
        try:
            page = requests.get(url)
            return page
        except Exception as ex:
            raise ex