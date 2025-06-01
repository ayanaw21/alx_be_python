task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")


match priority :
    case 'high' :
        reminder = f"'{task}' is a high priority task"
    case 'medium' : 
        reminder = f"'{task}' is medium priority task"
    case 'low':
        reminder = f"'{task}' is low priority task"
    case _:
        reminder = f"'{task}' has unknown priority"
if time_bound == "yes" :
    reminder+= " that requires immediate attention today!"
elif time_bound == "no":
    reminder += ". Consider completing it when you have free time."
    
print(reminder)
        
        