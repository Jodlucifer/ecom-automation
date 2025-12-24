from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure


class AddUser(BasePage):

    ADMIN = (By.XPATH, "//a[contains(@href,'viewAdminModule')]")
    BUTTON = (By.CSS_SELECTOR, "button[role='none']")
    ADD_BTN = (By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--secondary'][type='button']")
    USER_ROLE = (By.CSS_SELECTOR, "div[class='oxd-grid-2 orangehrm-full-width-grid'] div:nth-child(1) div:nth-child(1) div:nth-child(2) div:nth-child(1) div:nth-child(1) div:nth-child(2)")

    def __init__(self, driver, logger):

        super().__init__(driver)
        self.logger = logger


    def click_add_user_button(self):
        self.click(self.BUTTON)
        self.click(self.ADMIN)
        self.click(self.ADD_BTN)

    def select_dropdown(self, value):
        dropdown = self.wait_for_visible(self.USER_ROLE)
        dropdown.click()

        option = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//div[contains(@class,'oxd-select-dropdown') and contains(@class,'--position')]//span[normalize-space()='{value}']"
                )
            )
        )
        option.click()
