task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
  case "high":
    if time_bound == "yes":
      print(f"Reminder: {task} is high task that requires immediate attention today!")
  case "medium":
    if time_bound == "yes":
      print(f"Note: {task} might not be agent but try working on it soon.")
    else:
      print(f"Note: {task} seems not to be time sensitive.")
  case "low":
    if time_bound == "no":
      print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
