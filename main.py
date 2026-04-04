from common.driver import get_driver
from executor import execute_step
from common.report import log_result, save_report
from LLM import generate_steps_from_goal
from parser import parse_step

# Input
driver = get_driver()

goal = "login to facebook"

steps = generate_steps_from_goal(goal)

print("Generated Steps:")
for s in steps:
    print(s)
#######################
# Execution Loop
for step_no, step in enumerate(steps, start=1):
    step_json = parse_step(step)

    print("Parsed:", step_json)

    execute_step(driver, step, step_json)

# 🔥 VERY IMPORTANT
print("✅ Saving report...")
save_report()