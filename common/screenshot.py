import os
from datetime import datetime
import time

def take_screenshot(driver, step_name):
    folder = "screenshots"
    os.makedirs(folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = os.path.abspath(f"{folder}/{step_name}_{timestamp}.png")

    # 🔥 Important wait
    time.sleep(2)

    driver.save_screenshot(file_path)

    print("📸 Screenshot saved:", file_path)

    return file_path