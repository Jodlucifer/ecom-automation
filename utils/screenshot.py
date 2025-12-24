import os
from datetime import datetime

def capture_screenshot(driver, name):
    if not os.path.exists("logs/screenshots"):
        os.makedirs("logs/screenshots")

    file_name = f"logs/screenshots/{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    driver.save_screenshot(file_name)
    return file_name
