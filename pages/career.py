from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage
import time

class CareerPage(BasePage):
    LOCATIONS_BLOCK = (By.XPATH, "//section[contains(.,'Our Locations')]")
    TEAMS_BLOCK = (By.XPATH, "//section[contains(.,'Find your calling')]")
    LIFE_AT_INSIDER_BLOCK = (By.XPATH, "//h2[contains(text(),'Life at Insider')]")
    QA_JOBS_BUTTON = (By.XPATH, "//a[contains(@href,'quality-assurance') and contains(text(),'Quality Assurance')]")

    COOKIE_BANNER = (By.ID, "cookie-law-info-bar")

    def close_cookie_banner(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.COOKIE_BANNER))
            self.driver.execute_script(
                "var b=document.getElementById('cookie-law-info-bar'); if(b){b.style.display='none';}"
            )
        except:
            pass

    def is_all_blocks_visible(self):
        time.sleep(1)
        return (
            self.is_visible(self.LOCATIONS_BLOCK) and
            self.is_visible(self.TEAMS_BLOCK) and
            self.is_visible(self.LIFE_AT_INSIDER_BLOCK)
        )

    def go_to_qa_jobs(self):
        self.close_cookie_banner()
        try:
            self.click(self.QA_JOBS_BUTTON)
        except:
            
            self.driver.get("https://useinsider.com/careers/quality-assurance/")
        self.wait.until(lambda d: "quality-assurance" in d.current_url)