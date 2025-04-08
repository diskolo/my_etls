from abc import ABC, abstractmethod

import requests


class Requester(ABC):
    @abstractmethod
    def get(self, url):
        pass
