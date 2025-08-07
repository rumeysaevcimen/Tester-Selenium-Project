from selenium.webdriver.common.by import By
from pages.base import BasePage

class HomePage(BasePage):
    URL = "https://useinsider.com/"
    COMPANY_MENU = (By.XPATH, "//a[contains(text(),'Company')]")
    CAREERS_LINK = (By.XPATH, "//a[contains(text(),'Careers')]")

    def load(self):
        self.driver.get(self.URL)

    def go_to_careers_page(self):
        self.click(self.COMPANY_MENU)
        self.click(self.CAREERS_LINK)
