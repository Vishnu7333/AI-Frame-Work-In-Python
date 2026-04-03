import time
import re

def highlight(driver, element):
    driver.execute_script(
        "arguments[0].style.border='3px solid red'", element
    )
    time.sleep(0.3)

# Paasword 
def mask_value(value):
    if value:
        return "*" * len(value)
    return value

def mask_sensitive_step(step):
    # mask password
    if "password" in step.lower():
        return re.sub(r"(password\s+)(\S+)", r"\1******", step, flags=re.IGNORECASE)

    return step