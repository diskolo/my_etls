from abc import ABC, abstractmethod
from typing import List


class Parser(ABC):
    @abstractmethod
    def parse(self, html: str) -> List[dict]:
        raise NotImplementedError