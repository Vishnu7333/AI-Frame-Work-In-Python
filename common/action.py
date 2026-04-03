from common.utils import highlight

def click(driver, element):
    highlight(driver, element)
    element.click()

def send_keys(driver, element, value):
    highlight(driver, element)
    element.clear()
    element.send_keys(value)