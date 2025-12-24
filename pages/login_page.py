from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class LogIn(BasePage):
    """ LogIN page methods """

    USERNAME = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MSG = (By.CSS_SELECTOR, "p.oxd-alert-content-text")
    CONFIRM_MSG = (By.CSS_SELECTOR, "div.oxd-topbar-header-title")

    def __init__(self, driver, logger):
        super().__init__(driver)
        self.logger = logger

    @allure.step("Login with Credentials: Username :{username} Password {password}")
    def login(self, username, password):
        self.type_text(self.USERNAME, username)
        self.type_text(self.PASSWORD, password)
        self.click(self.SUBMIT)
        self.logger.info("Logging in with credentials: UserName: %s, Password : %s", username, password)


    @allure.step("Validate login result for Scenario: {scenario}")
    def validate_login(self, scenario, popup):
        if scenario == "ValidTestCase":
            self.wait.until(lambda d: "dashboard" in d.current_url.lower())
            confirm_msg = self.wait_for_visible(self.CONFIRM_MSG).text.lower()
            assert "dashboard" , confirm_msg
        else:
            error = self.wait_for_visible(self.ERROR_MSG).text.lower()
            assert error, popup




