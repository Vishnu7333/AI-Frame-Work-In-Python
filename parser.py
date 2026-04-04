def parse_step(step):
    step = step.lower()

    if step.startswith("open"):
        return {
            "action": "open",
            "value": step.split(" ", 1)[1]
        }

    elif "email" in step:
        return {
            "action": "send_keys",
            "locator": "name=email",
            "value": "your_email"
        }

    elif "password" in step:
        return {
            "action": "send_keys",
            "locator": "name=pass",
            "value": "your_password"
        }

    elif "click" in step and "login" in step:
        return {
            "action": "click",
            "locator": "xpath=//div[@aria-label='Log in']"
        }

    return {"action": "unknown"}