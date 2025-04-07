import pandas.testing as pdt
from expects import expect, be

from my_etls.extract.infrascture.real_python_scrapping import RealPythonScrapping
from tests.test_data import TestData


class TestRealPythonScrappingExtractor:
    def test_given_url_when_scrapping_return_dataframe(self):
        url = "https://realpython.github.io/fake-jobs/"
        expected = TestData.get_real_python_expected_dataframe()
        scrapper = RealPythonScrapping()

        results = scrapper.extract(url)

        expect(len(results)).to(be(100))
        pdt.assert_frame_equal(results[0:2], expected)
