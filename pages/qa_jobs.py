import time
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage


class QAPage(BasePage):
    SEE_ALL_QA_JOBS_BUTTON = (By.XPATH, "//a[contains(text(),'See all QA jobs')]")
    DEPARTMENT_DROPDOWN = (By.ID, "select2-filter-by-department-container")
    DEPARTMENT_RESULTS = (By.CSS_SELECTOR, "ul#select2-filter-by-department-results li")
    LOCATION_DROPDOWN = (By.ID, "select2-filter-by-location-container")
    LOCATION_RESULTS = (By.CSS_SELECTOR, "ul#select2-filter-by-location-results li")
    
    JOB_LIST_ITEMS = (By.CSS_SELECTOR, ".position-list-item-wrapper, .position-list-item")

    FIRST_VIEW_ROLE_BUTTON = (By.XPATH, "//a[text()='View Role' and contains(@class, 'btn-navy')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click_see_all_jobs(self):
        self.click(self.SEE_ALL_QA_JOBS_BUTTON)
        self.wait.until(lambda d: "open-positions" in d.current_url)
        self.wait.until(EC.presence_of_element_located(self.FIRST_VIEW_ROLE_BUTTON))

    def apply_filters(self, department="Quality Assurance", location="Istanbul, Turkiye"):
        # Department 
        self.click(self.DEPARTMENT_DROPDOWN)
        dept_options = self.wait.until(EC.presence_of_all_elements_located(self.DEPARTMENT_RESULTS))
        for opt in dept_options:
            if department.lower() in opt.text.lower():
                opt.click()
                break
        time.sleep(1)

        # Location 
        self.click(self.LOCATION_DROPDOWN)
        self.wait.until(EC.visibility_of_any_elements_located(self.LOCATION_RESULTS))

        loc_options = self.wait.until(EC.presence_of_all_elements_located(self.LOCATION_RESULTS))
        for opt in loc_options:
            if location.lower() in opt.text.lower():
                
                self.driver.execute_script("arguments[0].scrollIntoView(true);", opt)
                time.sleep(0.5)
                try:
                    opt.click()
                except Exception:
                    
                    self.driver.execute_script("arguments[0].click();", opt)
                break

        time.sleep(2)


    def validate_job_listings(self, department="Quality Assurance", location="Istanbul, Turkiye"):
        jobs = self.wait.until(EC.presence_of_all_elements_located(self.JOB_LIST_ITEMS))
        assert len(jobs) > 0, "No job listings found!"

        for index, job in enumerate(jobs, start=1):
            try:
                dept_text = job.find_element(By.CSS_SELECTOR, ".position-department").text
                loc_text = job.find_element(By.CSS_SELECTOR, ".position-location").text
            except StaleElementReferenceException:
                jobs = self.wait.until(EC.presence_of_all_elements_located(self.JOB_LIST_ITEMS))
                job = jobs[index - 1]
                dept_text = job.find_element(By.CSS_SELECTOR, ".position-department").text
                loc_text = job.find_element(By.CSS_SELECTOR, ".position-location").text

            print(f"DEBUG [{index}] Department text from page: '{dept_text}'")
            print(f"DEBUG [{index}] Location text from page: '{loc_text}'")

            if department.lower() not in dept_text.lower():
                print(f"⚠️ Bu ilan departman '{department}' değil, atlanıyor: {dept_text}")
                continue

            if not any(loc.lower() in loc_text.lower() for loc in location.split(", ")):
                print(f"⚠️ Bu ilan lokasyon '{location}' değil, atlanıyor: {loc_text}")
                continue

        print("✅ Tüm uygun ilanlar doğrulandı.")

    def click_first_view_role(self):
        self._hide_sticky_bar()
        time.sleep(1)

        buttons = self.driver.find_elements(*self.FIRST_VIEW_ROLE_BUTTON)
        if not buttons:
            raise Exception("Hiç 'View Role' butonu bulunamadı!")

        for btn in buttons:
            try:
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
                time.sleep(0.5)
                if btn.is_displayed() and btn.is_enabled():
                    try:
                        btn.click()
                        print("View Role butonuna tıklandı.")
                        return
                    except ElementClickInterceptedException:
                       
                        self._hide_sticky_bar()
                        time.sleep(0.5)
                        self.driver.execute_script("arguments[0].click();", btn)
                        print("View Role butonuna tıklandı (JS click ile).")
                        return
            except (ElementClickInterceptedException, StaleElementReferenceException) as e:
                print(f"Butona tıklama denemesi başarısız oldu, diğerine geçiliyor: {e}")
                continue

        raise Exception("Tıklanabilir 'View Role' butonu bulunamadı!")

    def _hide_sticky_bar(self):
        try:
            self.driver.execute_script("""
                var bar = document.querySelector('.cli-bar-container');
                if(bar){ bar.style.display='none'; }
            """)
        except Exception:
            pass


    def _safe_click(self, element):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(0.3)
            element.click()
        except ElementClickInterceptedException:
            self._hide_sticky_bar()
            time.sleep(0.5)
            element.click()
