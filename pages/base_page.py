from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """ Base Page Class That holds common web elements methods"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)


    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))


    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        self.clear(locator)
        self.wait_for_visible(locator).send_keys(text)

    def clear(self, locator):
        self.wait_for_visible(locator).clear()


