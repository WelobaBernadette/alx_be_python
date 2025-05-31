# daily_reminder.py

# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process and display customized reminder
match priority:
    case "high" | "medium" | "low":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"\nNote: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
    case _:
        print("\nInvalid priority entered. Please enter high, medium, or low.")
