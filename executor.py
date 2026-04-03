from common.locator import get_element
from common.action import click, send_keys
from common.screenshot import take_screenshot
from common.report import log_result
from common.utils import mask_value
from common.utils import mask_sensitive_step

def execute_step(driver, step, step_json):
    action = step_json.get("action")
    locator = step_json.get("locator")
    value = step_json.get("value")

    try:
        # 🔹 ACTION HANDLING
        if action == "open":
            driver.get(value)
            expected = f"Page should open: {value}"
            actual = f"Page opened: {driver.current_url}"

        elif action == "click":
            element = get_element(driver, locator)
            click(driver, element)
            expected = "User should be able to click element"
            actual = "Element clicked successfully"


        elif action == "send_keys":
           element = get_element(driver, locator)
           send_keys(driver, element, value)

           if "password" in step.lower():
              masked = mask_value(value)
              expected = "User should enter password"
              actual = f"Entered value: {masked}"
           else:
                expected = f"User should enter value: {value}"
                actual = f"Entered value: {value}"

        else:
            expected = "Valid action should be executed"
            actual = f"Unknown action: {action}"

        # ✅ SUCCESS
        screenshot = take_screenshot(driver, action)
        safe_step = mask_sensitive_step(step)
        log_result(safe_step, expected, actual, "PASS", screenshot)

    except Exception as e:
        print("❌ Error:", e)

        # ❌ FAILURE
        expected = "Action should be executed successfully"
        actual = str(e)

        screenshot = take_screenshot(driver, f"{action}_error")
        safe_step = mask_sensitive_step(step)
        log_result(safe_step, expected, actual, "FAIL", screenshot)