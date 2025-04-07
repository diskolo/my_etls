import pandas as pd


class TestData:
    @classmethod
    def get_real_python_expected_dataframe(cls) -> pd.DataFrame:
        positions = [
            {
                "position": "Senior Python Developer",
                "company": "Payne, Roberts and Davis",
                "location": "Stewartbury, AA",
                "position_date": "2021-04-08",
                "apply_url": "https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html",
            },
            {
                "position": "Energy engineer",
                "company": "Vasquez-Davidson",
                "location": "Christopherville, AA",
                "position_date": "2021-04-08",
                "apply_url": "https://realpython.github.io/fake-jobs/jobs/energy-engineer-1.html",
            },
        ]

        return pd.DataFrame(positions)
