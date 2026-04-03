from selenium.webdriver.common.by import By
from common.wait import wait_and_retry

def get_element(driver, locator):

    locators = []

    if locator.startswith("//"):
        locators.append((By.XPATH, locator))

    elif locator.startswith("name="):
        locators.append((By.NAME, locator.split("=")[1]))

    elif locator.startswith("id="):
        locators.append((By.ID, locator.split("=")[1]))

    elif locator.startswith(".") or locator.startswith("#"):
        locators.append((By.CSS_SELECTOR, locator))

    # 🔥 fallback locators
    if "login" in locator.lower():
        locators.append((By.XPATH, "//div[@aria-label='Log in']"))

    return wait_and_retry(driver, locators, condition="clickable")