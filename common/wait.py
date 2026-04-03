from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def wait_and_retry(driver,locators,condition="presence",timeout=10,retries=3,delay=1,):
    last_exception = None

    for attempt in range(retries):
        print(f"🔄 Retry Attempt {attempt + 1}")

        for by, value in locators:
            try:
                print(f"   🔍 Trying locator: {value}")

                wait = WebDriverWait(driver, timeout)

                # 🔹 condition handling
                if condition == "presence":
                    element = wait.until(
                        EC.presence_of_element_located((by, value))
                    )

                elif condition == "visible":
                    element = wait.until(
                        EC.visibility_of_element_located((by, value))
                    )

                elif condition == "clickable":
                    element = wait.until(
                        EC.element_to_be_clickable((by, value))
                    )

                else:
                    raise Exception(f"Unknown condition: {condition}")

                print("   ✅ Found element")
                return element

            except Exception as e:
                print(f"   ❌ Failed for locator: {value}")
                last_exception = e

        time.sleep(delay)

    raise Exception("❌ Element not found with any locator") from last_exception