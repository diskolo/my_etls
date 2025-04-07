import pandas as pd
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


class RealPythonScrapping:
    def extract(self, url: str) -> pd.DataFrame:
        scrapped_results = self._extract_job_results_from_page(url)

        job_results = self._transform_html_results_to_dataset(scrapped_results)

        return job_results

    @staticmethod
    def _extract_job_results_from_page(url: str) -> Tag:
        page = requests.get(url)

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find(id="ResultsContainer")
        return results

    @staticmethod
    def _transform_html_results_to_dataset(results) -> pd.DataFrame:
        job_cards = results.find_all("div", class_="card-content")
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

        jobs_df = pd.DataFrame(jobs)
        return jobs_df
