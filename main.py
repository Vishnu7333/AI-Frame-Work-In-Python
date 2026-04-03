from common.driver import get_driver
from executor import execute_step
from LLM import parse_step
from common.report import log_result, save_report

driver = get_driver()

with open("steps.txt") as f:
    steps = f.readlines()

for step in steps:
    step = step.strip()
    step_json = parse_step(step)

    print("Parsed:", step_json)

    execute_step(driver, step, step_json)

# 🔥 VERY IMPORTANT
print("✅ Saving report...")
save_report()