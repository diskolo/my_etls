from expects import expect, be, equal, raise_error

from my_etls.extract.domain.exceptions import RealPythonParserException
from my_etls.extract.infrastructure.real_python.real_python_parser import (
    RealPythonParser,
)
from tests.test_data import TestData


class TestRealPythonParser:
    def test_given_html_when_parser_then_return_list_of_elements_as_dict(self):
        html_page = TestData.get_html()
        expected_results = TestData.get_real_python_expected_elements()

        parser = RealPythonParser()

        results = parser.parse(html_page)

        expect(len(results)).to(be(2))
        expect(results).to(equal(expected_results))

    def test_given_html_when_parser_empty_page_then_raise_exception(self):
        empty_html = TestData.get_empty_html()

        parser = RealPythonParser()

        message = "Error parsing, empty content"
        expect(lambda: parser.parse(empty_html)).to(
            raise_error(RealPythonParserException, message)
        )
