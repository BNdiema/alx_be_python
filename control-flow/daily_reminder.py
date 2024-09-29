task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
  case "high":
    if priority == "high" and time_bound == "yes":
      print(f"{task} is high task that requires immediate attention today!")
  case "medium":
    if priority == "medium" and time_bound == "yes":
      print(f"{task} might not be agent but try working on it soon.")
    else:
      print(f"{task} seems not to be time sensitive.")
  case "low":
    if priority == "low" and time_bound == "no":
      print(f"{task} is a low priority task. Consider completing it when you have free time.")
