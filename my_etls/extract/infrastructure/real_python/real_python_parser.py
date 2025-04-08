from typing import List

from bs4 import BeautifulSoup

from my_etls.extract.domain.exceptions import RealPythonParserException
from my_etls.extract.domain.parser import Parser


class RealPythonParser(Parser):
    def parse(self, html: str) -> List[dict]:
        soup = BeautifulSoup(html, "html.parser")
        results = soup.find(id="ResultsContainer")
        job_cards = results.find_all("div", class_="card-content")

        if not job_cards:
            message = "Error parsing, empty content"
            raise RealPythonParserException(message)

        jobs = []
        for job_card in job_cards:
            title_element = job_card.find("h2", class_="title").text.strip()
            company_element = job_card.find("h3", class_="company").text.strip()
            location_element = job_card.find("p", class_="location").text.strip()
            tittle_date = job_card.find("time").text.strip()
            apply_url = job_card.find_all(
                "a", string=lambda a_href: "apply" in a_href.text.lower()
            )[0]["href"].strip()
            job = {
                "position": title_element,
                "company": company_element,
                "location": location_element,
                "position_date": tittle_date,
                "apply_url": apply_url,
            }
            jobs.append(job)

        return jobs
