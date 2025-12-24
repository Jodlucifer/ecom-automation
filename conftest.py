import pytest
import yaml
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():

    with open("D:\work_env\dev\ecom-automation\config\config.yaml", "r") as f:
        config = yaml.safe_load(f)

    driver= webdriver.Chrome()
    driver.get(config["url"])
    driver.maximize_window()

    yield driver

    if driver:
        driver.close()
        driver.quit()