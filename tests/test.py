import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from pages.home import HomePage
from pages.career import CareerPage
from pages.qa_jobs import QAPage

class InsiderTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_full_flow(self):
        try:
            home = HomePage(self.driver)
            home.load()
            self.assertIn("Insider", self.driver.title)

            home.go_to_careers_page()
            career = CareerPage(self.driver)
            self.assertTrue(career.is_all_blocks_visible())

            career.go_to_qa_jobs()
            qa = QAPage(self.driver)
            qa.click_see_all_jobs()
            qa.apply_filters(
                department="Quality Assurance",
                location="Istanbul, Turkiye"
            )

            qa.validate_job_listings()

            
            qa.click_first_view_role()

            
            self.driver.switch_to.window(self.driver.window_handles[-1])
            time.sleep(2)  

            self.assertIn("lever", self.driver.current_url)

        except Exception:
            self.driver.save_screenshot("test_failure.png")
            raise

if __name__ == "__main__":
    unittest.main()
