import pandas.testing as pdt
from doublex import Mimic, Stub, Spy
from expects import expect, be, raise_error

from my_etls.extract.domain.exceptions import RealPythonScrapperException
from my_etls.extract.infrastructure.http_requester import HttpRequester
from my_etls.extract.infrastructure.real_python.real_python_parser import RealPythonParser
from my_etls.extract.infrastructure.real_python.real_python_scraper import (
    RealPythonScrapper,
)
from tests.test_data import TestData


class TestRealPythonScraper:
    def test_given_url_when_scrapping_return_dataframe(self):
        url = "https://realpython.github.io/fake-jobs/"
        expected = TestData.get_real_python_expected_dataframe()
        requester = HttpRequester()
        parser = RealPythonParser()
        scrapper = RealPythonScrapper(requester, parser)

        results = scrapper.scrape(url)

        expect(len(results)).to(be(100))
        pdt.assert_frame_equal(results[0:2], expected)

    def test_given_url_when_request_get_error(self):
        url = "https://realpython.github.io/fake-jobs/"
        with Mimic(Stub, HttpRequester) as http_requester:
            http_requester.get(url).raises(Exception)

        parser = Mimic(Spy, RealPythonParser)

        scrapper = RealPythonScrapper(http_requester, parser)
        message = "Error on get request for https://realpython.github.io/fake-jobs/"
        expect(lambda: scrapper.scrape(url)).to(
            raise_error(RealPythonScrapperException, message)
        )
