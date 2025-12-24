from pages.login_page import LogIn
from utils.logger import get_logger
from utils.screenshot import capture_screenshot
from pages.admin_add_user_page import AddUser

logger = get_logger(__name__)

def test_login(driver):
     login = LogIn(driver, logger)
     login.login("admin", "admin123")
     login.validate_login("ValidTestCase", "invalid credentials")
     capture_screenshot(driver, "login")



# def test_add_user(driver):
#      add_user = AddUser(driver, logger)
#
#      add_user.click_add_user_button()
#      add_user.select_dropdown("Admin")
#      print("HI")