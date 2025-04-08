from typing import List

import pandas as pd


class TestData:
    @classmethod
    def get_real_python_expected_elements(cls) -> List[dict]:
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

        return positions

    @classmethod
    def get_html(cls) -> str:
        return """
        <body>
   <section class="section">
      <div class="container mb-5">
         <h1 class="title is-1">
            Fake Python
         </h1>
         <p class="subtitle is-3">
            Fake Jobs for Your Web Scraping Journey
         </p>
      </div>
      <div class="container">
         <div id="ResultsContainer" class="columns is-multiline">
            <div class="column is-half">
               <div class="card">
                  <div class="card-content">
                     <div class="media">
                        <div class="media-left">
                           <figure class="image is-48x48">
                              <img src="https://files.realpython.com/media/real-python-logo-thumbnail.7f0db70c2ed2.jpg?__no_cf_polish=1" alt="Real Python Logo">
                           </figure>
                        </div>
                        <div class="media-content">
                           <h2 class="title is-5">Senior Python Developer</h2>
                           <h3 class="subtitle is-6 company">Payne, Roberts and Davis</h3>
                        </div>
                     </div>
                     <div class="content">
                        <p class="location">Stewartbury, AA</p>
                        <p class="is-small has-text-grey">
                           <time datetime="2021-04-08">2021-04-08</time>
                        </p>
                     </div>
                     <footer class="card-footer">
                        <a href="https://www.realpython.com" target="_blank" class="card-footer-item">Learn</a>
                        <a href="https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html" target="_blank" class="card-footer-item">Apply</a>
                     </footer>
                  </div>
               </div>
            </div>
            <div class="column is-half">
               <div class="card">
                  <div class="card-content">
                     <div class="media">
                        <div class="media-left">
                           <figure class="image is-48x48"><img src="https://files.realpython.com/media/real-python-logo-thumbnail.7f0db70c2ed2.jpg?__no_cf_polish=1" alt="Real Python Logo"></figure>
                        </div>
                        <div class="media-content">
                           <h2 class="title is-5">Energy engineer</h2>
                           <h3 class="subtitle is-6 company">Vasquez-Davidson</h3>
                        </div>
                     </div>
                     <div class="content">
                        <p class="location">Christopherville, AA</p>
                        <p class="is-small has-text-grey">
                           <time datetime="2021-04-08">2021-04-08</time>
                        </p>
                     </div>
                     <footer class="card-footer">
                        <a href="https://www.realpython.com" target="_blank" class="card-footer-item">Learn</a>
                        <a href="https://realpython.github.io/fake-jobs/jobs/energy-engineer-1.html" target="_blank" class="card-footer-item">Apply</a>
                     </footer>
                  </div>
               </div>
            </div>
         </div>
      </div>
   </section>
</body>
        """

    @classmethod
    def get_empty_html(cls):
        return  """
        <body>
            <section class="section">
                <div class="container mb-5">
                    <h1 class="title is-1">
                         Fake Python
                    </h1>
                    <p class="subtitle is-3">
                        Fake Jobs for Your Web Scraping Journey
                    </p>
                </div>
                <div class="container">
                    <div id="ResultsContainer" class="columns is-multiline"></div>
                </div>
            </section>
        </body>"""

    @classmethod
    def get_real_python_expected_dataframe(cls):
        return pd.DataFrame(cls.get_real_python_expected_elements())
