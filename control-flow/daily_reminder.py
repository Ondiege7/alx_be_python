# 1. Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# 2. Process the Task Based on Priority and Time Sensitivity
# We use Match Case to handle the priority levels
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' is a task with an undefined priority"

# 3. Refine the reminder based on time sensitivity
if time_bound == "yes":
    # Add the immediate attention message
    reminder += " that requires immediate attention today!"
    print(f"Reminder: {reminder}")
else:
    # Add the low-urgency message
    reminder += ". Consider completing it when you have free time."
    print(f"Note: {reminder}")