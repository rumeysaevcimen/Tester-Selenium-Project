from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click(self, by_locator):
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.3)
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    def is_visible(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).is_displayed()

    def get_text(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).text

    def find_elements(self, by_locator):
        return self.driver.find_elements(*by_locator)

    def take_screenshot(self, name="screenshot.png"):
        self.driver.save_screenshot(name)
