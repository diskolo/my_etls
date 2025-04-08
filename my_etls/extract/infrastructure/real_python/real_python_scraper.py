import pandas as pd
from bs4.element import Tag

from my_etls.extract.domain.exceptions import RealPythonScrapperException, RealPythonParserException
from my_etls.extract.domain.parser import Parser
from my_etls.extract.domain.requester import Requester
from my_etls.extract.infrastructure.real_python.real_python_parser import RealPythonParser


class RealPythonScrapper:
    def __init__(self, html_requester: Requester, real_python_parser: Parser):
        self._html_requester = html_requester
        self._real_python_parser = real_python_parser

    def scrape(self, url: str) -> pd.DataFrame:
        try:
            page = self._html_requester.get(url)

            jobs = self._real_python_parser.parse(page.content)

            job_results = pd.DataFrame(jobs)

            return job_results
        except RealPythonParserException as pe:
            raise pe
        except Exception as ex:
            message = f"Error on get request for {url}"
            raise RealPythonScrapperException(message) from ex